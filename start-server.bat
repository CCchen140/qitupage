@echo off
chcp 65001 >nul
echo Starting local server...
echo Please visit http://localhost:8080
echo Press Ctrl+C to stop the server
echo.

:: Start the server in background
start /b python -m http.server 8080

:: Wait a moment for server to start
timeout /t 2 /nobreak >nul

:: Open browser
start http://localhost:8080
