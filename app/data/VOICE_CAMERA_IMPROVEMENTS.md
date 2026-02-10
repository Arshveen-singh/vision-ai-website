# Voice & Camera Mode Improvements

## Changes Made

### 1. Chat Mode Access from Voice & Camera Modes

**Problem:** Users couldn't access chat mode while using voice or camera features.

**Solution:** Added a "Switch to Chat" button in both modes.

#### Voice Mode (`VoiceMode.tsx`)
- Added `MessageSquare` icon button in the header
- Button positioned in top-left corner
- Accepts `onSwitchToChat` callback prop
- Smooth transition to chat mode

#### Camera Mode (`GestureControls.tsx`)
- Added `MessageSquare` icon button in the header
- Button positioned next to title
- Accepts `onSwitchToChat` callback prop
- Allows quick switch without losing camera state

#### App Integration (`App.tsx`)
- Updated both component calls to pass `onSwitchToChat={() => setActiveTab('chat')}`
- Seamless tab switching

### 2. Groq Whisper Integration Fix

**Problem:** Voice recognition wasn't using Groq's Whisper model consistently.

**Solution:** Enhanced voice handler to prioritize Groq Whisper with better logging.

#### Voice Handler (`ai_core/voice_handler.py`)
- Added debug logging to show which STT model is being used
- Groq Whisper Large V3 is now always preferred when available
- Clear status messages:
  - `✅ Groq Whisper transcribed: [text]` - When using Groq
  - `⚠️ Using Google STT (Groq not available): [text]` - Fallback
  - `🎤 Groq Whisper: [text]` - In continuous listening mode

#### Backend (`backend/app/api/v1/endpoints/voice.py`)
- Already correctly sets `app.voice.groq_handler = app.groq`
- Lazy initialization ensures Groq handler is always available
- No changes needed - working as intended

## How It Works

### Voice Recognition Flow:
```
User speaks
    ↓
Audio captured by microphone
    ↓
Check if groq_handler is available
    ↓
YES: Use Groq Whisper Large V3 (preferred)
    ↓
    - Save audio to temp WAV file
    - Call groq_handler.transcribe_audio()
    - Delete temp file
    - Return transcribed text
    ↓
NO: Fallback to Google Speech Recognition
    ↓
    - Use recognizer.recognize_google()
    - Return transcribed text
```

### Chat Mode Switching:
```
User in Voice/Camera Mode
    ↓
Clicks MessageSquare button
    ↓
onSwitchToChat() callback triggered
    ↓
setActiveTab('chat') called in App.tsx
    ↓
React re-renders with ChatInterface
    ↓
User now in chat mode
```

## UI Changes

### Voice Mode
```
┌─────────────────────────────────────┐
│  [💬]  Voice Command                │  ← Chat button added
│  Interact with Vision AI naturally  │
├─────────────────────────────────────┤
│                                     │
│         [Audio Visualizer]          │
│                                     │
├─────────────────────────────────────┤
│  [🔇] [🎤] [🔊]                     │
└─────────────────────────────────────┘
```

### Camera Mode
```
┌─────────────────────────────────────┐
│  [💬] Vision Control    [🎤] [🔊]   │  ← Chat button added
│  Hand tracking & Mood detection     │
├─────────────────────────────────────┤
│                                     │
│         [Camera Feed]               │
│                                     │
└─────────────────────────────────────┘
```

## Testing

### Test Voice Recognition:
1. Start the app
2. Go to Voice Mode
3. Click microphone button
4. Speak clearly
5. Check console/status for:
   - `🎤 Groq Whisper: [your text]` (if Groq is working)
   - `⚠️ Using Google STT` (if Groq unavailable)

### Test Chat Mode Switching:
1. Go to Voice Mode
2. Click the MessageSquare (💬) button in top-left
3. Should switch to Chat Mode
4. Repeat for Camera Mode

### Verify Groq Whisper:
1. Check backend logs for Groq API calls
2. Status messages should show "Groq Whisper" not "Google STT"
3. If seeing Google STT, check:
   - Groq API key is set
   - Backend is running
   - `app.voice.groq_handler` is not None

## Benefits

### User Experience:
- ✅ Quick access to chat from any mode
- ✅ No need to navigate through sidebar
- ✅ Seamless mode switching
- ✅ Better voice recognition accuracy

### Technical:
- ✅ Uses Groq's Whisper Large V3 (state-of-the-art)
- ✅ Graceful fallback to Google STT
- ✅ Clear logging for debugging
- ✅ Proper error handling

## Troubleshooting

### Voice Recognition Not Working:
1. Check microphone permissions
2. Verify Groq API key is set
3. Check backend logs for errors
4. Look for status messages in console

### Chat Button Not Appearing:
1. Verify you're on Voice or Camera mode
2. Check browser console for errors
3. Ensure App.tsx is passing the callback

### Using Google STT Instead of Groq:
1. Check if Groq API key is valid
2. Verify backend is running
3. Check if `app.voice.groq_handler` is set
4. Look for initialization errors in backend logs

## Future Enhancements

- [ ] Add keyboard shortcut for mode switching (e.g., Ctrl+C for chat)
- [ ] Show which STT model is active in UI
- [ ] Add voice model selector (Whisper variants)
- [ ] Implement voice activity detection (VAD)
- [ ] Add noise cancellation
- [ ] Support multiple languages in Whisper
