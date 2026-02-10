# Vision AI

A privacy-first AI assistant built for people who care about their data.

## What Makes This Different

Most AI tools force you online, lock you into subscriptions, and hide what they do with your data. Vision AI takes a different approach:

✅ **Works offline** - Local mode by default, no internet required  
✅ **Your API keys** - Bring your own, no subscription needed  
✅ **Complete transparency** - See every cloud request in real-time  
✅ **Military-grade encryption** - AES-256 for all conversations  
✅ **Desktop-native** - Real system integration, not just a web wrapper  
✅ **Multi-modal** - Chat, voice, vision, gestures, automation  
✅ **Open source** - MIT license, inspect and modify freely  

## Quick Start

### Installation

1. **Check your system:**
   ```bash
   CHECK_SYSTEM.bat
   ```

2. **Install dependencies:**
   ```bash
   INSTALL_DEPENDENCIES.bat
   ```

3. **Launch the app:**
   ```bash
   START_VISION_AI.bat
   ```

That's it! The setup wizard will guide you through the rest.

### First Steps

1. Complete the setup wizard
2. Choose Local Mode (default) or enable Cloud Mode
3. Set up encrypted memory storage
4. Start chatting!

## Features

### Privacy-First Architecture
- **Local Mode:** Everything runs on your machine
- **Cloud Mode:** Optional, with full transparency
- **Encrypted Storage:** AES-256 encryption for conversations
- **Network Logging:** See exactly what data is sent

### Flexible AI Integration
- **Groq:** Free, lightning-fast responses
- **OpenAI:** GPT-4, GPT-3.5 Turbo
- **Anthropic:** Claude 3 models
- **Local Models:** LM Studio, Ollama, any OpenAI-compatible API

### Multi-Modal Interface
- **Chat:** Natural language conversations
- **Voice:** Speech-to-text and text-to-speech
- **Vision:** OCR, image analysis, gesture recognition
- **Automation:** Control your PC with natural language

### Desktop Experience
- Native Electron app
- System integration
- Quick actions and widgets
- Customizable themes

## Documentation

### Getting Started
- [Installation Guide](docs/setup/INSTALLATION.md)
- [Quick Start](docs/setup/QUICK_START.md)
- [System Requirements](docs/setup/SYSTEM_REQUIREMENTS.md)

### User Guides
- [User Manual](docs/guides/USER_MANUAL.md)
- [API Configuration](docs/guides/API_CONFIGURATION.md)
- [Privacy Guide](docs/guides/PRIVACY_GUIDE.md)
- [Troubleshooting](docs/guides/TROUBLESHOOTING.md)

### Security & Privacy
- [Security Overview](docs/security/SECURITY_OVERVIEW.md)
- [Privacy Policy](docs/security/PRIVACY_POLICY.md)
- [Encryption Details](docs/security/ENCRYPTION.md)

### For Developers
- [Architecture](docs/development/ARCHITECTURE.md)
- [Contributing](docs/development/CONTRIBUTING.md)
- [Building from Source](docs/development/BUILDING.md)
- [API Reference](docs/development/API_REFERENCE.md)

## System Requirements

**Minimum:**
- Intel i3 or equivalent
- 4GB RAM
- Windows 10+
- Python 3.8+
- Node.js (LTS)

**Recommended:**
- Intel i5 or better
- 8GB RAM
- SSD storage

## Security

Vision AI takes security seriously:

- **AES-256 encryption** for all stored conversations
- **Local-first architecture** minimizes data exposure
- **Content firewall** blocks harmful content
- **PII protection** automatically redacts sensitive data
- **Audit logging** tracks all security events
- **Open source** for community review

See [Security Overview](docs/security/SECURITY_OVERVIEW.md) for details.

## Privacy

Your data, your control:

- **Local Mode:** No data leaves your device
- **Cloud Mode:** Explicit consent required
- **Transparent logging:** See every network request
- **No telemetry:** We don't track you
- **GDPR compliant:** Right to access, delete, export

See [Privacy Policy](docs/security/PRIVACY_POLICY.md) for details.

## Contributing

We welcome contributions! See [Contributing Guide](docs/development/CONTRIBUTING.md) for:
- Code style guidelines
- Development setup
- Testing requirements
- Pull request process

## Testing

Comprehensive test suite covering:
- Security (authentication, encryption, firewall)
- Privacy (data isolation, network transparency)
- Integration (end-to-end workflows)
- Performance (memory, response time)

Run tests:
```bash
pytest
```

See [Test Suite](tests/README.md) for details.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Disclaimer

Vision AI is provided as-is. Users are responsible for:
- Their own API keys and associated costs
- Compliance with third-party API terms of service
- Securing their local data and encryption keys
- Any automation commands executed through the app

See [Legal Risk Assessment](docs/security/LEGAL_RISK_ASSESSMENT.md) for details.

## Support

- [Documentation](docs/README.md)
- [GitHub Issues](https://github.com/yourusername/vision-ai/issues)
- [Troubleshooting Guide](docs/guides/TROUBLESHOOTING.md)

## Roadmap

- [ ] Mobile app (iOS/Android)
- [ ] Plugin system
- [ ] Multiple API key profiles
- [ ] Advanced automation workflows
- [ ] Team collaboration features

## Acknowledgments

Built with:
- [Electron](https://www.electronjs.org/) - Desktop framework
- [FastAPI](https://fastapi.tiangolo.com/) - Backend API
- [React](https://reactjs.org/) - UI framework
- [MediaPipe](https://mediapipe.dev/) - Gesture recognition

## Star History

If you find Vision AI useful, consider giving it a star! ⭐

---

**Made with ❤️ for people who care about privacy**
