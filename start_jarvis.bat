@echo off
cd /d "%~dp0"
python -m pip install -r requirements.txt
start "JARVIS Server" cmd /k python backend\server.py
timeout /t 3 >nul
start "" frontend\index.html
