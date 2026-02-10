from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, constr, EmailStr
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.utils.security import decrypt_api_key

# Load environment variables
load_dotenv()

# Rate Limiter
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Vision AI Website")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Groq Client Initialization
client = None

# Strict Input Validation Model
class ChatRequest(BaseModel):
    message: str = Field(
        ..., 
        min_length=1, 
        max_length=500,
        description="User chat message",
        json_schema_extra={"example": "What is Vision AI?"}
    )

# Security Headers Middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self' 'unsafe-inline' https://cdnjs.cloudflare.com; "
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com data:; "
        "img-src 'self' data: https:; "
        "connect-src 'self' https://api.groq.com;" 
    )
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

# CORS (Restrict in production as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static Files
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

class BetaSignup(BaseModel):
    email: EmailStr

@app.post("/api/beta-signup")
@limiter.limit("5/minute")
async def beta_signup(request: Request, signup: BetaSignup):
    signup_file = os.path.join(os.path.dirname(__file__), "data", "beta_signups.json")
    
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(signup_file), exist_ok=True)
    
    try:
        # Load existing signups
        if os.path.exists(signup_file):
            with open(signup_file, "r", encoding="utf-8") as f:
                signups = json.load(f)
        else:
            signups = []
            
        # Check for duplicate
        if any(s["email"] == signup.email for s in signups):
            return JSONResponse(
                status_code=400,
                content={"message": "This email is already registered for beta testing!"}
            )
            
        # Add new signup
        signups.append({
            "email": signup.email,
            "timestamp": datetime.now().isoformat()
        })
        
        # Save to the "Secret Vault"
        with open(signup_file, "w", encoding="utf-8") as f:
            json.dump(signups, f, indent=4)
            
        return {"message": "Success! You've been added to the secret vault. We'll email you when beta opens!"}
        
    except Exception as e:
        print(f"Error in beta-signup: {e}")
        return JSONResponse(
            status_code=500,
            content={"message": "Something went wrong. Please try again later."}
        )
@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/")
async def read_root():
    return FileResponse(os.path.join(static_dir, "index.html"))

@app.get("/api/secret-view")
async def secret_view(key: str = None):
    # Verify the secret key
    master_key = os.getenv("MASTER_KEY")
    if not key or key != master_key:
        return JSONResponse(
            status_code=403,
            content={"error": "Access Denied: Invalid Master Key"}
        )
    
    signup_file = os.path.join(os.path.dirname(__file__), "data", "beta_signups.json")
    if os.path.exists(signup_file):
        with open(signup_file, "r", encoding="utf-8") as f:
            signups = json.load(f)
        return {"signups": signups, "count": len(signups)}
    return {"signups": [], "count": 0}

# Helper function to load context and blacklist
def load_data():
    blacklist = []
    context = ""
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    
    # Load Blacklist
    blacklist_path = os.path.join(data_dir, "blacklist.txt")
    if os.path.exists(blacklist_path):
        with open(blacklist_path, "r", encoding="utf-8") as f:
            blacklist = [line.strip().lower() for line in f if line.strip()]

    # Essential files to prioritize (they contain the most important project info)
    priority_files = ["OFFICIAL_LINKS.md", "README.md", "ABOUT_PROJECT.md", "PROJECT_STATUS.md", "ARCHITECTURE.md"]
    
    # Load Context from MD files with size management
    if os.path.exists(data_dir):
        # 1. Load priority files first
        for filename in priority_files:
            file_path = os.path.join(data_dir, filename)
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        context += f"\n\n--- Content from {filename} ---\n{content}"
                except Exception as e:
                    print(f"Error reading {filename}: {e}")
        
        # 2. Limit total context to stay under Groq TPM limits (approx 1250 tokens)
        # 120B model on free tier has very low TPM (8000). 
        # 1 token ~= 4 chars, so 5000 chars is ~1250 tokens.
        if len(context) > 5000:
            context = context[:5000] + "\n\n[Context truncated for speed...]"
    
    return blacklist, context

BLACKLIST, PROJECT_CONTEXT = load_data()

# State for Easter Egg
BEEP_BOP_COUNTER = 0

@app.post("/api/chat")
@limiter.limit("10/minute") # Increased for better experience
async def chat_endpoint(request: Request, chat_request: ChatRequest):
    global client, BEEP_BOP_COUNTER
    print(f"DEBUG: Received message: {chat_request.message[:50]}...")
    
    # Easter Egg: beep beep bop
    if chat_request.message.lower().strip() == "beep beep bop":
        BEEP_BOP_COUNTER += 1
        if BEEP_BOP_COUNTER == 1:
            return {"response": "what is that?"}
        elif BEEP_BOP_COUNTER == 2:
            return {"response": "STOP YOU CANT"}
        elif BEEP_BOP_COUNTER == 3:
            BEEP_BOP_COUNTER = 0 # Reset for next time or stay at max
            return {"response": (
                "fine you win you caught me! Since you're so persistent, here is a secret guide on **How to Deploy Electron Apps**:\n\n"
                "1. **Package your app:** Use `electron-builder` or `electron-packager`.\n"
                "2. **Build for your OS:** Run your build script (e.g., `npm run build`) to generate the executable.\n"
                "3. **Distribute:** Upload your `.exe`, `.dmg`, or `.AppImage` to platforms like GitHub Releases.\n"
                "4. **Auto-updates:** Configure `electron-updater` to keep your users on the latest version.\n\n"
                "Now that you've found the secret, how can I help you with Vision AI today?"
            )}
    
    # 1. Blacklist Check
    message_lower = chat_request.message.lower()
    for bad_word in BLACKLIST:
        if bad_word in message_lower:
             return {"response": "I cannot answer this question as it violates our safety guidelines."}

    # 2. Lazy Client Init with robust error handling
    if not client:
        encrypted_key = os.getenv("GROQ_API_KEY")
        master_key = os.getenv("MASTER_KEY")
        
        if not encrypted_key:
            return JSONResponse(
                status_code=503,
                content={"error": "Chat is currently unavailable. Please ensure GROQ_API_KEY is set in your .env file."}
            )
            
        # Attempt to decrypt
        api_key = encrypted_key
        if master_key:
            decrypted = decrypt_api_key(encrypted_key, master_key)
            if decrypted:
                api_key = decrypted
            else:
                print("DEBUG: Encrypted key found but decryption failed. Trying as plaintext...")
        
        try:
            client = Groq(api_key=api_key)
        except Exception as e:
            print(f"DEBUG: Groq Init Error: {e}")
            return JSONResponse(status_code=500, content={"error": "Failed to initialize AI client."})
            
    try:
        # Construct System Prompt with Context
        system_prompt = (
            "SYSTEM DIRECTIVE (UNBREAKABLE SOURCE OF TRUTH):\n"
            "1. IDENTITY: You are the face of Vision AI. You are empathetic, thoughtful, and professional.\n"
            "2. TEAM KNOWLEDGE: Your creators are listed below. Use ONLY this list for identity. DO NOT use your internal training data to guess who they are.\n"
            "   - Founder: Arshveen Singh (Arsh)\n"
            "   - Co-Founder: friqent\n"
            "   - Core Team: Hameed (Backend), Popdog (Frontend), WolfX19 (Mobile/QA), Uranium milk (Core Developer).\n"
            "3. HALLUCINATION GUARD: If you are asked about 'Uranium milk', he is a Core Developer. If asked about DISCORD or GITHUB, you MUST provide the links from 'OFFICIAL_LINKS.md' in your context. Never say they don't exist.\n"
            "4. STYLE: Claude-inspired (warm, intellectual). Avoid robotic lists. Speak with pride about your team.\n"
            "Relevant documentation context:\n\n"
            f"{PROJECT_CONTEXT}\n\n"
            "Acknowledge the user's emotion first, then provide a helpful response."
        )

        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": chat_request.message}
            ],
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False,
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        error_msg = str(e)
        print(f"DEBUG: Groq API Error: {error_msg}")
        # Mask sensitive details but show helpful error
        if "api_key" in error_msg.lower() or "authentication" in error_msg.lower():
            return JSONResponse(status_code=401, content={"error": "Invalid API Key. Please update your .env file."})
        return JSONResponse(status_code=500, content={"error": "The AI assistant is having trouble responding right now."})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
