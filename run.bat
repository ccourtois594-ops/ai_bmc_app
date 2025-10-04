@echo off
echo Demarrage de BMC...
cd /d "%~dp0"
call .venv\Scripts\activate.bat
streamlit run app.py --server.port=8501

pause
