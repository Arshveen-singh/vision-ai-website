# VISION AI - Complete Technical Documentation

> **Version:** 1.0.0  
> **Created by:** Arshveen Singh  
> **Last Updated:** January 2026  
> **Repository:** https://github.com/gitus-droid/VISION-AI-DEV

---

## Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Technology Stack](#technology-stack)
4. [Core Components](#core-components)
5. [AI Models & Capabilities](#ai-models--capabilities)
6. [Frontend Applications](#frontend-applications)
7. [Backend API](#backend-api)
8. [Security System](#security-system)
9. [Modes of Operation](#modes-of-operation)
10. [Features Deep Dive](#features-deep-dive)
11. [File Structure](#file-structure)
12. [API Reference](#api-reference)
13. [Configuration](#configuration)
14. [Dependencies](#dependencies)

---

## Overview

**Vision AI** is an intelligent multi-source personal assistant that combines:
- Multiple AI models via Groq API
- Voice control (speech-to-text and text-to-speech)
- OCR (Optical Character Recognition)
- Gesture recognition with mood detection
- PC automation and control
- Multi-source intelligence (Wikipedia, DuckDuckGo, Groq LLM)

### Key Highlights
- **Creator:** Arshveen Singh, Class 9 student from Kamal Public School, West Delhi, India
- **Built:** November-December 2025
- **Purpose:** Research, homework help, coding assistance, PC automation, and general AI assistance

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        VISION AI SYSTEM                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Electron App │  │   Web App    │  │  Python CLI  │          │
│  │   (React)    │  │  (Next.js)   │  │              │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
│         │                 │                 │                   │
│         └────────────┬────┴────────────────┘                   │
│                      │                                          │
│              ┌───────▼───────┐                                  │
│              │ FastAPI       │                                  │
│              │ Backend       │                                  │
│              │ (Port 8000)   │                                  │
│              └───────┬───────┘                                  │
│                      │                                          │
│  ┌───────────────────┼───────────────────┐                     │
│  │                   │                   │                     │
│  ▼                   ▼                   ▼                     │
│ ┌────────┐    ┌────────────┐    ┌─────────────┐               │
│ │AI Core │    │  Security  │    │   Modes     │               │
│ │        │    │            │    │             │               │
│ │-Groq   │    │-Firewall   │    │-Normal      │               │
│ │-Voice  │    │-Auth       │    │-Fun         │               │
│ │-OCR    │    │-Audit      │    │-Hacker      │               │
│ │-Gesture│    │-Encryption │    │             │               │
│ │-Search │    │            │    │             │               │
│ └────────┘    └────────────┘    └─────────────┘               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

### Backend (Python)
| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| Framework | FastAPI | Latest | REST API server |
| AI Provider | Groq API | Latest | LLM, STT, TTS, Vision |
| OCR | EasyOCR | Latest | Text extraction from images |
| Voice STT | Groq Whisper Large V3 | - | Speech recognition |
| Voice TTS | PlayAI TTS via Groq | - | Speech synthesis |
| Gesture | MediaPipe | Latest | Hand tracking |
| Mood Detection | FER | Latest | Facial emotion recognition |
| Search | DuckDuckGo | - | Web search |
| Knowledge | Wikipedia API | - | Encyclopedia queries |
| Security | JWT, bcrypt | - | Authentication |

### Frontend - Desktop App (Electron)
| Component | Technology | Version |
|-----------|------------|---------|
| Framework | Electron | 28.2.1 |
| UI Library | React | 18.2.0 |
| Build Tool | Vite | 5.1.0 |
| Styling | Tailwind CSS | 3.4.1 |
| UI Components | Radix UI, shadcn/ui | Latest |
| Animations | Framer Motion | 11.18.2 |
| HTTP Client | Axios | 1.6.7 |
| Icons | Lucide React | 0.323.0 |

### Frontend - Web App (Next.js)
| Component | Technology | Version |
|-----------|------------|---------|
| Framework | Next.js | 14+ |
| Language | TypeScript | Latest |
| Styling | Tailwind CSS | Latest |
| Theme | next-themes | Latest |

### Frontend - Mobile (Flutter)
| Component | Technology |
|-----------|------------|
| Framework | Flutter |
| Language | Dart |

---

## Core Components

### 1. AI Core (`ai_core/`)

#### `groq_handler.py` - Main AI Interface
Handles all Groq API interactions with specialized models:

```python
# Available Methods:
- transcribe_audio(file_path, language)     # Whisper Large V3 STT
- generate_speech(text, voice)              # PlayAI TTS
- analyze_image(image_path, prompt)         # Vision analysis
- generate_reasoning(query, context)        # Complex reasoning
- generate_multilingual(query, language)    # Multi-language support
- call_function(query, tools)               # Function calling
- check_safety(text)                        # Content safety check
- generate_response(query, mode)            # General text response
- parse_automation_command(query)           # NL to automation
```

#### `voice_handler.py` - Voice Control
- Speech recognition via Groq Whisper or Google fallback
- Text-to-speech via PlayAI TTS or pyttsx3 fallback
- Continuous listening mode
- Voice command processing

#### `ocr_handler.py` - Text Extraction
- Image OCR using EasyOCR
- PDF text extraction
- Supports: PNG, JPG, JPEG, BMP, GIF, TIFF, PDF
- Max file size: 10MB

#### `gesture_controller.py` - Gesture Recognition
- Hand tracking via MediaPipe
- Gesture detection: swipe, point, open palm, fist, peace, thumbs up
- Mood detection via FER (Facial Emotion Recognition)
- App-specific gesture mappings (Instagram, YouTube, etc.)

#### `pc_automation.py` - System Control
- Open applications (Calculator, Notepad, Chrome, Spotify, etc.)
- Open URLs and social media
- System controls (volume, brightness, media playback)
- Gesture-based control integration
- Natural language command parsing

#### `search_handler.py` - Web Search
- DuckDuckGo instant answers
- DuckDuckGo web search
- Result formatting

#### `wikipedia_handler.py` - Knowledge Base
- Wikipedia article search
- Summary extraction
- Multi-language support

#### `source_router.py` - Query Routing
- Automatic source selection based on query type
- Manual override with `/wiki`, `/duck`, `/groq`, `/auto` prefixes
- Keyword-based routing logic

---

## AI Models & Capabilities

### Groq Model Registry

| Model Type | Model ID | Use Case |
|------------|----------|----------|
| **Text (Default)** | `moonshotai/kimi-k2-instruct-0905` | General responses |
| **STT** | `whisper-large-v3` | Speech-to-text |
| **TTS** | `playai/playai-tts` | Text-to-speech |
| **Vision** | `meta-llama/llama-4-maverick-17b-128e-instruct` | Image analysis |
| **Reasoning** | `qwen/qwen3-32b` | Complex logic |
| **Multilingual** | `meta-llama/llama-3.3-70b-versatile` | Multi-language |
| **Function Calling** | `moonshotai/kimi-k2-instruct` | Tool use |
| **Safety** | `meta-llama/llama-guard-4-12b` | Content moderation |

### TTS Voices Available
- `Arista-PlayAI` (default female)
- `Angelo-PlayAI` (male)
- `Arsenio-PlayAI`
- `Cillian-PlayAI`
- `And more...`

---

## Frontend Applications

### Desktop App (Electron + React)

**Location:** `electron-app/`

**Views:**
1. **Dashboard** - System metrics, quick actions
2. **Chat Interface** - Main AI conversation
3. **Voice Mode** - JARVIS-like voice interaction
4. **Gesture Controls** - Hand gesture settings
5. **Settings** - Configuration panel

**Key Components:**
```
electron-app/src/
├── components/
│   ├── ChatInterface.tsx    # Main chat UI
│   ├── ChatMessage.tsx      # Message bubbles
│   ├── Dashboard.tsx        # Metrics dashboard
│   ├── VoiceMode.tsx        # Voice control UI
│   ├── GestureControls.tsx  # Gesture settings
│   ├── SettingsView.jsx     # Settings panel
│   ├── Sidebar.tsx          # Navigation
│   └── ui/                  # Reusable UI components
├── services/
│   └── api.ts               # Backend API client
├── context/
│   └── AppContext.tsx       # Global state
└── hooks/
    └── useChat.ts           # Chat logic hook
```

**Running Desktop App:**
```bash
cd electron-app
npm install
npm run electron:dev
```

### Web App (Next.js)

**Location:** `vision_ai_web/`

**Features:**
- Server-side rendering
- Theme support (dark/light)
- Responsive design
- Chat components with animations

**Running Web App:**
```bash
cd vision_ai_web
npm install
npm run dev
```

### Python CLI

**Location:** `vision_ai_app.py`

**Commands:**
- `/wiki <query>` - Force Wikipedia search
- `/duck <query>` - Force DuckDuckGo search
- `/groq <query>` - Force Groq AI response
- `/ocr <file>` - Extract text from image
- `fun <password>` - Enter Fun Mode
- `hacker <password>` - Enter Hacker Mode
- `normal` - Return to Normal Mode
- `exit` - Quit application

---

## Backend API

**Location:** `backend/app/`

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root - API info |
| GET | `/health` | Health check |
| GET | `/status` | System status |
| GET | `/security/scan` | Security status |
| POST | `/api/v1/chat` | Send chat message |
| POST | `/api/v1/chat/stream` | Streaming chat |
| GET | `/api/v1/status` | Vision AI status |
| POST | `/api/v1/settings` | Update settings |
| POST | `/api/v1/mode` | Switch mode |
| POST | `/api/v1/ocr` | OCR processing |
| POST | `/api/v1/voice/transcribe` | Speech-to-text |
| POST | `/api/v1/voice/speak` | Text-to-speech |

### Running Backend:
```bash
cd backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

---

## Security System

### Components

#### 1. Content Firewall (`security/firewall.py`)
- Blocks harmful content
- Sanitizes output
- Permanent protection across all modes

#### 2. Authentication (`security/authentication.py`)
- Password hashing with bcrypt
- Mode-specific passwords
- API key management

#### 3. Audit Logger (`security/audit.py`)
- Logs all queries
- Tracks mode switches
- Records failed login attempts
- Command execution logging

#### 4. JWT Authentication (`backend/app/core/auth.py`)
- Token-based API authentication
- Session management

#### 5. AI Firewall (`backend/app/core/ai_firewall.py`)
- Request validation
- Rate limiting
- Threat detection

### Security Features
- Rate limiting (100 requests/hour default)
- CORS protection
- Security headers (XSS, CSRF, etc.)
- Input sanitization
- Device allowlist for Hacker Mode
- Command whitelisting

---

## Modes of Operation

### 1. Normal Mode (Default)
- Professional, helpful responses
- Full firewall protection
- Standard AI capabilities
- No special permissions

### 2. Fun Mode 🎉
- Password protected
- More casual, playful responses
- Uses emojis
- Can discuss edgy topics
- **30-minute auto-timeout**
- Firewall still active

### 3. Hacker Mode 🔴
- Developer-only access
- Password protected
- Shell command execution
- Device allowlist required
- Rate-limited commands
- Full audit logging
- Whitelisted commands only

---

## Features Deep Dive

### Voice Control (JARVIS Mode)
```
Speech Recognition:
├── Primary: Groq Whisper Large V3
└── Fallback: Google Speech Recognition

Text-to-Speech:
├── Primary: PlayAI TTS via Groq
└── Fallback: pyttsx3 (offline)
```

### Gesture Control
```
Supported Gestures:
├── Swipe Left/Right → Navigate
├── Point → Select/Click
├── Open Palm → Pause
├── Fist → Play/Resume
├── Peace Sign → Screenshot
└── Thumbs Up → Like/Approve

App-Specific Mappings:
├── Instagram: Swipe for reels, point to like
├── YouTube: Swipe for videos, point for play/pause
└── Default: Scroll, click, pause
```

### Mood Detection
- Real-time facial emotion recognition
- Emotions: Happy, Sad, Angry, Surprised, Neutral, Fear, Disgust
- Confidence threshold: 60%
- Mood history tracking
- Potential for mood-based responses

### PC Automation
```
Supported Actions:
├── Open Apps: Calculator, Notepad, Chrome, Spotify, Discord, etc.
├── Open URLs: YouTube, Instagram, Twitter, Gmail, etc.
├── System: Volume, brightness, media controls
├── Info: Time, date, battery status
└── Gesture: Start/stop gesture control
```

### Multi-Source Intelligence
```
Query Routing:
├── "What is X" → Wikipedia
├── "Latest news about X" → DuckDuckGo
├── "Open X" → PC Automation
└── Everything else → Groq AI
```

---

## File Structure

```
VISION_AI/
├── ai_core/                    # Core AI modules
│   ├── __init__.py
│   ├── ai_brain.py            # Central AI coordinator
│   ├── groq_handler.py        # Groq API interface
│   ├── voice_handler.py       # Voice I/O
│   ├── ocr_handler.py         # OCR processing
│   ├── gesture_controller.py  # Gesture recognition
│   ├── pc_automation.py       # System automation
│   ├── search_handler.py      # Web search
│   ├── wikipedia_handler.py   # Wikipedia API
│   ├── source_router.py       # Query routing
│   ├── camera_handler.py      # Camera access
│   ├── model_registry.py      # AI model config
│   └── proactive_monitor.py   # Background monitoring
│
├── backend/                    # FastAPI backend
│   └── app/
│       ├── main.py            # App entry point
│       ├── api/v1/            # API routes
│       │   ├── api.py
│       │   └── endpoints/
│       │       ├── automation.py
│       │       ├── desktop.py
│       │       ├── vision.py
│       │       └── voice.py
│       ├── core/              # Core utilities
│       │   ├── config.py
│       │   ├── auth.py
│       │   ├── database.py
│       │   ├── ai_firewall.py
│       │   └── encryption.py
│       └── models/
│           └── user.py
│
├── electron-app/              # Desktop application
│   ├── electron/
│   │   ├── main.js           # Electron main process
│   │   └── preload.js        # Preload script
│   ├── src/
│   │   ├── App.tsx           # React root
│   │   ├── components/       # UI components
│   │   ├── services/         # API services
│   │   ├── context/          # React context
│   │   └── hooks/            # Custom hooks
│   └── package.json
│
├── vision_ai_web/             # Next.js web app
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── globals.css
│   ├── components/
│   └── lib/
│
├── vision_ai_flutter/         # Flutter mobile app
│   ├── lib/
│   │   └── main.dart
│   └── pubspec.yaml
│
├── modes/                     # Operation modes
│   ├── __init__.py
│   ├── normal_mode.py
│   ├── fun_mode.py
│   └── hacker_mode.py
│
├── security/                  # Security modules
│   ├── __init__.py
│   ├── authentication.py
│   ├── firewall.py
│   └── audit.py
│
├── services/                  # Business services
│   └── user_service.py
│
├── ui/                        # Python UI (Flet/CLI)
│   ├── __init__.py
│   ├── cli.py
│   ├── chat_view.py
│   ├── dashboard_view.py
│   └── settings_view.py
│
├── tests/                     # Test files
├── data/                      # Data storage
├── logs/                      # Log files
├── assets/                    # Static assets
│
├── vision_ai_app.py          # Main Python entry
├── flet_app.py               # Flet UI entry
├── config.ini                # Configuration
├── requirements.txt          # Python dependencies
├── .env.example              # Environment template
└── README.md                 # Quick start guide
```

---

## API Reference

### Chat Endpoint

**POST** `/api/v1/chat`

Request:
```json
{
  "message": "What is the capital of France?",
  "mode": "normal",
  "source_override": null
}
```

Response:
```json
{
  "success": true,
  "response": "The capital of France is Paris...",
  "source": "groq",
  "latency_ms": 245.3,
  "mode": "normal"
}
```

### Streaming Chat

**POST** `/api/v1/chat/stream`

Returns Server-Sent Events (SSE) with reasoning steps:
```
data: {"type": "step", "step_id": "firewall", "label": "Security Check", "status": "active"}
data: {"type": "step", "step_id": "firewall", "status": "complete"}
data: {"type": "step", "step_id": "routing", "label": "Routing Query", "status": "active"}
data: {"type": "response", "success": true, "response": "..."}
```

### Settings

**POST** `/api/v1/settings`

```json
{
  "default_source": "auto",
  "default_voice": "female",
  "theme": "dark",
  "groq_model": "moonshotai/kimi-k2-instruct-0905"
}
```

---

## Configuration

### Environment Variables (`.env`)

```bash
# Required
GROQ_API_KEY=your_groq_api_key

# Security (generate with: python -c "import secrets; print(secrets.token_urlsafe(32))")
SECRET_KEY=your_secret_key
ENCRYPTION_KEY=your_encryption_key
VISION_AI_API_KEY=your_local_api_key

# Optional - Voice
ELEVENLABS_API_KEY=your_elevenlabs_key

# Optional - OAuth
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret

# Optional - Database
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=vision_ai

# App Settings
DEBUG=false
```

### Config File (`config.ini`)

```ini
[SETTINGS]
default_source = auto
default_voice = female
theme = dark
groq_model = moonshotai/kimi-k2-instruct-0905

[PASSWORDS]
fun_mode_password_hash = <bcrypt_hash>
hacker_mode_password_hash = <bcrypt_hash>

[DEVICE_ALLOWLIST]
my_pc = 127.0.0.1
```

---

## Dependencies

### Python (`requirements.txt`)
```
groq>=0.4.0
fastapi>=0.109.0
uvicorn>=0.27.0
python-dotenv>=1.0.0
colorama>=0.4.6
wikipedia>=1.4.0
duckduckgo-search>=4.1.0
easyocr>=1.7.0
SpeechRecognition>=3.10.0
pyttsx3>=2.90
pygame>=2.5.0
mediapipe>=0.10.0
fer>=22.5.0
opencv-python>=4.9.0
pyautogui>=0.9.54
psutil>=5.9.0
bcrypt>=4.1.0
python-jose>=3.3.0
slowapi>=0.1.9
```

### Node.js (Electron App)
```json
{
  "react": "^18.2.0",
  "electron": "^28.2.1",
  "vite": "^5.1.0",
  "tailwindcss": "^3.4.1",
  "axios": "^1.6.7",
  "framer-motion": "^11.18.2",
  "lucide-react": "^0.323.0",
  "@radix-ui/*": "latest"
}
```

---

## Quick Start Commands

```bash
# Clone repository
git clone https://github.com/gitus-droid/VISION-AI-DEV.git
cd VISION-AI-DEV

# Setup environment
cp .env.example .env
# Edit .env with your API keys

# Install Python dependencies
pip install -r requirements.txt

# Run Python CLI
python vision_ai_app.py

# Run Backend
cd backend
uvicorn app.main:app --reload

# Run Desktop App
cd electron-app
npm install
npm run electron:dev

# Run Web App
cd vision_ai_web
npm install
npm run dev
```

---

## Support & Links

- **Repository:** https://github.com/gitus-droid/VISION-AI-DEV
- **Groq API:** https://console.groq.com/keys
- **ElevenLabs:** https://elevenlabs.io/

---

*This documentation is auto-generated and maintained for Vision AI v1.0.0*
