Write-Host "Cleaning old build..."
Remove-Item -Recurse -Force .\build\ -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force .\dist\ -ErrorAction SilentlyContinue
Remove-Item -Force .\MP3Player.spec -ErrorAction SilentlyContinue

Write-Host "Building new EXE..."
pyinstaller --onedir --windowed --icon=icon.ico mp3.py

Write-Host "Build Completed!"
Write-Host "Opening Output Folder..."
explorer.exe .\dist\
