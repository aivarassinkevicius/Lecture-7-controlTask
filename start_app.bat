@echo off
echo Starting AI Exercise Routine Generator...
echo.

REM Check if Ollama is installed
where ollama >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Ollama is not installed or not in PATH.
    echo Please install Ollama from https://ollama.ai
    pause
    exit /b 1
)

echo Checking Ollama service...
curl -s http://localhost:11434/api/tags >nul 2>nul
if %errorlevel% neq 0 (
    echo Starting Ollama service...
    start "Ollama" ollama serve
    timeout /t 5 /nobreak >nul
    echo Waiting for Ollama to start...
    timeout /t 3 /nobreak >nul
)

echo Checking if required AI models are available...
ollama list | find "gemma2:2b" >nul
if %errorlevel% neq 0 (
    echo Downloading gemma2:2b model... (smaller model, better for limited RAM)
    ollama pull gemma2:2b
)

ollama list | find "gemma3:270m" >nul
if %errorlevel% neq 0 (
    echo Downloading gemma3:270m model... (ultra-light model)
    ollama pull gemma3:270m
)

echo.
echo Starting the Exercise Routine Generator app...
echo Open your browser and go to: http://localhost:8501
echo Press Ctrl+C to stop the application
echo.

cd /d "%~dp0"
.venv\Scripts\activate && python -m streamlit run app.py

pause