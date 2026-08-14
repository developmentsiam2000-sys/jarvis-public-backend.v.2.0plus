@echo off
python -m pip install pyinstaller
pyinstaller --onefile --name JARVIS backend\server.py
pause
