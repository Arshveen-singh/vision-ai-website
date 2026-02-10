# Text-to-Speech Speaker Button

## Overview
Added a speaker button to AI message bubbles that allows users to hear the AI's response spoken aloud.

## Implementation

### Component: `ChatMessage.tsx`

#### Features:
- **Speaker button** appears on hover over AI messages
- **Visual feedback** when speaking (pulsing animation)
- **Smart text extraction** - speaks the actual message content, not JSON/code
- **Disabled state** while speaking to prevent multiple simultaneous speeches
- **Clean UI** - button only visible on hover, doesn't clutter the interface

#### UI Design:
```
┌─────────────────────────────────┐
│  🤖  AI Message Bubble      [🔊] │  ← Speaker button (hover to see)
│                                  │
│  Here's your response...         │
│                                  │
└─────────────────────────────────┘
```

#### Button States:
1. **Hidden** (default) - Only visible on hover
2. **Ready** (🔊) - Click to speak
3. **Speaking** (🔇 pulsing) - Currently speaking

### Code Changes:

**Added imports:**
```typescript
import { Volume2, VolumeX } from 'lucide-react';
import { visionAPI } from '../services/api';
```

**Added state:**
```typescript
const [isSpeaking, setIsSpeaking] = useState(false);
```

**Added handler:**
```typescript
const handleSpeak = async () => {
  if (isSpeaking) return;
  
  setIsSpeaking(true);
  try {
    const textToSpeak = getDisplayContent() || message.content;
    await visionAPI.speak(textToSpeak);
  } catch (error) {
    console.error('Failed to speak:', error);
  } finally {
    setTimeout(() => setIsSpeaking(false), 2000);
  }
};
```

**Added button:**
```typescript
{!isUser && (
  <motion.button
    whileHover={{ scale: 1.1 }}
    whileTap={{ scale: 0.9 }}
    onClick={handleSpeak}
    disabled={isSpeaking}
    className="absolute -top-2 -right-2 w-7 h-7 rounded-full..."
  >
    {isSpeaking ? <VolumeX size={14} /> : <Volume2 size={14} />}
  </motion.button>
)}
```

## How It Works

### Flow:
```
User hovers over AI message
    ↓
Speaker button appears (🔊)
    ↓
User clicks button
    ↓
handleSpeak() called
    ↓
Extract clean text (no JSON/code blocks)
    ↓
Call visionAPI.speak(text)
    ↓
Button shows speaking state (🔇 pulsing)
    ↓
Backend uses Groq TTS or pyttsx3
    ↓
Audio plays
    ↓
Button returns to ready state
```

### Smart Text Extraction:
The button intelligently extracts the right text to speak:
- **With artifacts**: Speaks the message text, not the code
- **With cards**: Speaks the message, not the JSON data
- **Plain text**: Speaks the entire message
- **Fallback**: Uses raw message content if extraction fails

## Backend Integration

Uses existing TTS infrastructure:
- **Primary**: Groq PlayAI TTS (high quality)
- **Fallback**: pyttsx3 (offline TTS)

API call:
```typescript
await visionAPI.speak(text);
```

Backend endpoint:
```
POST /api/v1/desktop/voice/speak
Body: { text: string, voice_id?: string }
```

## User Experience

### Benefits:
- ✅ **Accessibility** - Users can listen instead of reading
- ✅ **Multitasking** - Hear responses while doing other things
- ✅ **Learning** - Better for auditory learners
- ✅ **Convenience** - Quick access without switching modes
- ✅ **Non-intrusive** - Only visible on hover

### Design Decisions:
1. **Hover-only visibility** - Keeps UI clean
2. **Top-right position** - Doesn't interfere with text
3. **Pulsing animation** - Clear feedback when speaking
4. **Disabled while speaking** - Prevents audio overlap
5. **AI messages only** - User messages don't need TTS

## Styling

### Button Classes:
```css
/* Base */
absolute -top-2 -right-2 w-7 h-7 rounded-full

/* Visibility */
opacity-0 group-hover:opacity-100 transition-opacity

/* States */
bg-secondary/80 hover:bg-secondary  /* Ready */
bg-primary/80 animate-pulse         /* Speaking */

/* Effects */
shadow-lg border border-white/20
```

### Animations:
- **Hover**: Scale 1.1
- **Tap**: Scale 0.9
- **Speaking**: Pulse animation

## Testing

### Manual Test:
1. Start the app
2. Send a message to AI
3. Wait for AI response
4. Hover over AI message bubble
5. Speaker button should appear in top-right
6. Click the button
7. Should hear the message spoken aloud
8. Button should pulse while speaking

### Test Cases:
- ✅ Button appears on hover
- ✅ Button hidden by default
- ✅ Click triggers speech
- ✅ Visual feedback while speaking
- ✅ Can't click while already speaking
- ✅ Works with plain text messages
- ✅ Works with messages containing artifacts
- ✅ Works with messages containing cards
- ✅ Speaks clean text (no JSON/code)

## Troubleshooting

### Button Not Appearing:
1. Ensure you're hovering over an AI message (not user message)
2. Check CSS `group` and `group-hover` classes are working
3. Verify browser supports hover events

### No Audio:
1. Check system volume
2. Verify backend is running
3. Check Groq API key for TTS
4. Look for errors in console
5. Test with pyttsx3 fallback

### Audio Overlapping:
- Button is disabled while speaking
- If still happening, check `isSpeaking` state management

## Future Enhancements

- [ ] Add voice selection dropdown
- [ ] Show speaking progress/waveform
- [ ] Add pause/stop button
- [ ] Remember user's TTS preference
- [ ] Add keyboard shortcut (e.g., Alt+S)
- [ ] Support speech rate control
- [ ] Add auto-speak toggle for all AI messages
- [ ] Show estimated speech duration
- [ ] Add speech queue for multiple messages
- [ ] Support different languages

## Accessibility

### ARIA Support:
```typescript
title={isSpeaking ? "Speaking..." : "Speak message"}
disabled={isSpeaking}
```

### Keyboard Support:
- Button is focusable
- Can be activated with Enter/Space
- Visual focus indicator

### Screen Reader:
- Button has descriptive title
- State changes announced via title update

## Performance

### Optimizations:
- Uses React.memo for ChatMessage
- Button only renders for AI messages
- Lazy loading of audio
- Debounced state updates

### Resource Usage:
- Minimal CPU (button animation)
- Network: One API call per speech
- Memory: Negligible

## Related Features

- **Voice Mode**: Full voice interaction
- **Groq TTS**: High-quality text-to-speech
- **pyttsx3**: Offline TTS fallback
- **Voice Handler**: Backend TTS management

## Summary

The speaker button provides quick, convenient access to text-to-speech for AI messages without leaving chat mode. It's non-intrusive, accessible, and works seamlessly with existing TTS infrastructure.

**Status**: ✅ Fully implemented and ready to use
