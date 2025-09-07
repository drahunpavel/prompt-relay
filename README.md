## Prompt Relay

Prompt Relay is a containerized speech‑to‑text stack: a React web UI, a FastAPI UI gateway, an ASR API powered by Faster‑Whisper, and an optional Telegram bot.

### Core services
- **ASR API (`POST /api/asr/transcribe`)**: Converts audio to 16 kHz mono WAV and transcribes with Faster‑Whisper.
- **UI API gateway (`POST /api/ui/transcribe`)**: Proxies client uploads to the ASR API.
- **Web app**: Chat‑style UI to record/upload audio (≤15 MB) and view results.
- **Telegram bot**: aiogram bot for sending audio to transcription.

### Intended use
- **Use the web UI** or **call the HTTP endpoints** directly.
- **Deploy with Docker Compose**; web, UI API, and ASR services are exposed.