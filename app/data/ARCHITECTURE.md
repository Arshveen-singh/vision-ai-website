╔════════════════════════════════════════════════════════════════════════════╗
║              VISION AI DESKTOP APPLICATION - ARCHITECTURE                  ║
╚════════════════════════════════════════════════════════════════════════════╝

APPLICATION STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────────┐
│                        VISION AI DESKTOP APP                                │
│                    (flet_app.py - VisionAIDesktopApp)                       │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
            ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
            │   Sidebar    │  │  Chat Area   │  │  Input Bar   │
            │   (250px)    │  │  (Right)     │  │  (Bottom)    │
            └──────────────┘  └──────────────┘  └──────────────┘
                    │               │               │
                    │               │               │
            ┌───────┴─────────┐     │     ┌─────────┴──────────┐
            │                 │     │     │                    │
            ▼                 ▼     ▼     ▼                    ▼
        ┌─────────┐      ┌─────────┐  ┌─────────┐      ┌──────────────┐
        │  Logo   │      │ Messages│  │ Welcome │      │  TextField   │
        │         │      │ (List)  │  │ Message │      │              │
        └─────────┘      └─────────┘  └─────────┘      └──────────────┘
            │                 │
            │                 ├─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
        ┌─────────┐      ┌──────────┐      ┌──────────┐
        │   Mode  │      │   User   │      │    AI    │
        │Indicator│      │ Messages │      │ Messages │
        └─────────┘      │(Turquoise)      │(Gray)    │
            │            └──────────┘      └──────────┘
            │
        ┌───┴──────────────────────────────┐
        │                                  │
        ▼                                  ▼
    ┌─────────────┐              ┌──────────────┐
    │Mode Buttons │              │Send Button   │
    │ • Normal    │              │(Turquoise)   │
    │ • Fun       │              │     ✈️       │
    │ • Hacker    │              └──────────────┘
    └─────────────┘
        │
        ▼
    ┌─────────────────────┐
    │ Source Override     │
    │ • Wikipedia         │
    │ • DuckDuckGo        │
    │ • Groq AI           │
    └─────────────────────┘
        │
        ▼
    ┌─────────────┐
    │  Settings   │
    │     ⚙️      │
    └─────────────┘


DATA FLOW
═══════════════════════════════════════════════════════════════════════════════

USER INPUT
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ send_message()                                              │
│ • Get message from input field                              │
│ • Clear input field                                         │
│ • Add user message to chat (right-aligned, turquoise)       │
│ • Show loading indicator                                    │
│ • Call process_query_async()                                │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ process_query_async() [ASYNC]                               │
│ • Run in thread pool (non-blocking)                         │
│ • Call vision_ai.process_query(message)                     │
│ • Get response from VisionAI                                │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ VisionAI.process_query()                                    │
│ • Firewall check                                            │
│ • Route query (auto or forced source)                       │
│ • Call appropriate handler:                                 │
│   - Wikipedia.search()                                      │
│   - SearchHandler.search_duckduckgo_web()                   │
│   - GroqHandler.generate_response()                         │
│ • Log query                                                 │
│ • Return response                                           │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ Back to process_query_async()                               │
│ • Remove loading indicator                                  │
│ • Add AI message to chat (left-aligned, gray)               │
│ • Show source indicator                                     │
│ • Reset force_source                                        │
│ • Auto-scroll to bottom                                     │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
CHAT UPDATED


MODE SWITCHING FLOW
═══════════════════════════════════════════════════════════════════════════════

USER CLICKS MODE BUTTON
    │
    ├─ Normal Mode ──────────────────────────────────────────┐
    │                                                         │
    │  switch_mode("normal")                                 │
    │  • Update vision_ai.mode = "normal"                    │
    │  • Update mode indicator                               │
    │  • Show success message                                │
    │                                                         │
    └─────────────────────────────────────────────────────────┘
    │
    ├─ Fun/Hacker Mode ─────────────────────────────────────┐
    │                                                         │
    │  show_password_dialog()                                │
    │  • Show password input dialog                          │
    │  • User enters password                                │
    │  • Call vision_ai.switch_mode(mode, password)          │
    │  • If valid:                                           │
    │    - switch_mode(mode)                                 │
    │    - Close dialog                                      │
    │  • If invalid:                                         │
    │    - Show error                                        │
    │    - Keep dialog open                                  │
    │                                                         │
    └─────────────────────────────────────────────────────────┘


SOURCE OVERRIDE FLOW
═══════════════════════════════════════════════════════════════════════════════

USER CLICKS SOURCE BUTTON
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ show_source_indicator()                                     │
│ • Set force_source = "wikipedia|duckduckgo|groq"            │
│ • Show message: "Using [Source] for next query"             │
└─────────────────────────────────────────────────────────────┘
    │
    ▼
USER SENDS MESSAGE
    │
    ▼
┌─────────────────────────────────────────────────────────────┐
│ process_query_async()                                       │
│ • Check if force_source is set                              │
│ • If set: use that source                                   │
│ • If not: auto-route based on query                         │
│ • After response: reset force_source = None                 │
└─────────────────────────────────────────────────────────────┘


CLASS HIERARCHY
═══════════════════════════════════════════════════════════════════════════════

VisionAIDesktopApp
│
├── page (ft.Page)
│   └── Flet page instance
│
├── vision_ai (VisionAI)
│   ├── groq (GroqHandler)
│   ├── wiki (WikipediaHandler)
│   ├── search (SearchHandler)
│   ├── firewall (ContentFirewall)
│   └── audit (AuditLogger)
│
├── current_mode (str)
│   └── "normal" | "fun" | "hacker"
│
├── force_source (str | None)
│   └── "wikipedia" | "duckduckgo" | "groq" | None
│
├── chat_list (ft.ListView)
│   └── Message containers
│
├── input_field (ft.TextField)
│   └── User input
│
├── mode_indicator (ft.Container)
│   └── Current mode display
│
└── loading_container (ft.Container)
    └── Loading indicator


COMPONENT TREE
═══════════════════════════════════════════════════════════════════════════════

Page
│
└── Row (Main Container)
    │
    ├── Container (Sidebar)
    │   └── Column
    │       ├── Text (Logo)
    │       ├── Container (Mode Indicator)
    │       ├── Container (Mode Buttons)
    │       │   ├── Container (Normal)
    │       │   ├── Container (Fun)
    │       │   └── Container (Hacker)
    │       ├── Divider
    │       ├── Text (Source Override)
    │       ├── Container (Source Buttons)
    │       │   ├── Container (Wikipedia)
    │       │   ├── Container (DuckDuckGo)
    │       │   └── Container (Groq AI)
    │       ├── Container (Spacer)
    │       └── Container (Settings)
    │
    └── Container (Main Chat Area)
        └── Column
            ├── Container (Chat Display)
            │   └── ListView
            │       ├── Container (Welcome)
            │       ├── Container (User Message)
            │       ├── Container (Loading)
            │       └── Container (AI Message)
            │
            └── Container (Input Bar)
                └── Row
                    ├── TextField (Input)
                    └── Container (Send Button)


STYLING HIERARCHY
═══════════════════════════════════════════════════════════════════════════════

Colors
├── Primary: #40E0D0 (Turquoise)
├── Background: #0f172a (Dark Blue)
├── Sidebar: #1a1a2e (Darker Blue)
├── Cards: #1e293b (Dark Gray)
├── Text: #ffffff (White)
└── Hover: #1e3a5f (Light Blue)

Typography
├── Logo: 24px Bold
├── Mode: 13px Bold
├── Messages: 14px Normal
├── Buttons: 12-13px Normal
└── Labels: 11-12px Bold

Effects
├── Border Radius: 12-16px
├── Shadows: Drop shadows on cards
├── Transitions: Smooth animations
├── Hover: Color and border changes
└── Glass: Transparency on input bar


ASYNC ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════

Main Thread (UI)
│
├── send_message()
│   └── Synchronous
│       ├── Add user message
│       ├── Show loading
│       └── Create async task
│
└── process_query_async()
    └── Async coroutine
        ├── asyncio.to_thread()
        │   └── Thread Pool
        │       └── vision_ai.process_query()
        │           ├── API calls
        │           └── Processing
        │
        └── page.update()
            └── UI refresh


INTEGRATION POINTS
═══════════════════════════════════════════════════════════════════════════════

Vision AI Desktop App
        │
        ├─────────────────────────────────────────────────────┐
        │                                                     │
        ▼                                                     ▼
    VisionAI Class                                    Flet Framework
    (vision_ai_app.py)                               (flet package)
        │                                                     │
        ├── GroqHandler                              ├── ft.Page
        ├── WikipediaHandler                         ├── ft.Container
        ├── SearchHandler                            ├── ft.Column
        ├── ContentFirewall                          ├── ft.Row
        ├── AuditLogger                              ├── ft.ListView
        └── Config                                   ├── ft.TextField
                                                     ├── ft.Button
                                                     ├── ft.Text
                                                     ├── ft.Dialog
                                                     └── ft.ProgressRing


ERROR HANDLING
═══════════════════════════════════════════════════════════════════════════════

Try Block (process_query_async)
│
├── Success Path
│   ├── Remove loading
│   ├── Add AI message
│   └── Update UI
│
└── Exception Path
    ├── Remove loading
    ├── Add error message
    └── Log exception


═══════════════════════════════════════════════════════════════════════════════
Version: 1.0.0
Framework: Flet 0.20.0+
Status: Production Ready
═══════════════════════════════════════════════════════════════════════════════
