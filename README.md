# JARVIS AI v2

A ChatGPT-style JARVIS application using a local Ollama model.

Features:
- AI chat and conversation memory
- Chat history
- File upload and TXT/MD/code/JSON/CSV/PDF context
- Web-search support
- Browser speech recognition
- Browser text-to-speech
- Dark/light mode
- Responsive UI
- Windows launcher and EXE build script

## Windows

Install dependencies:
```powershell
python -m pip install -r requirements.txt
```

Install Ollama and get a model:
```powershell
ollama pull qwen2.5:0.5b
```

Start:
```powershell
python backend/server.py
```

Then open `frontend/index.html`.

For a stronger model, if your computer can run it:
```powershell
$env:JARVIS_MODEL="qwen2.5:3b"
python backend/server.py
```

The EXE helper is `build_exe.bat`. The browser frontend is still needed unless you package the frontend separately.

This is a JARVIS application, not the actual ChatGPT model.
