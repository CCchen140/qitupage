# Start local server script
Write-Host "Starting local server..." -ForegroundColor Green
Write-Host "Please visit http://localhost:8080" -ForegroundColor Cyan
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host ""

# Start server in background job
$job = Start-Job { python -m http.server 8080 }

# Wait for server to start
Start-Sleep -Seconds 2

# Open browser
Start-Process "http://localhost:8080"

# Keep script running to maintain the job
Write-Host "Server is running in background. Press Enter to stop." -ForegroundColor Yellow
Read-Host

# Stop the job when user presses Enter
Stop-Job $job
Remove-Job $job
Write-Host "Server stopped." -ForegroundColor Green
