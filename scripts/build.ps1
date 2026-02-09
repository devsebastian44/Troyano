# Build Script for Troyano (Educational)

Write-Host "Starting Build Process..."

# Check for PyArmor
if (Get-Command "pyarmor" -ErrorAction SilentlyContinue) {
    Write-Host "PyArmor found. Obfuscating payload..."
    # pyarmor gen src/payload/troyano.py
    Write-Host "Obfuscation skipped (Uncomment in script to enable)."
} else {
    Write-Host "PyArmor not found. Install it with: pip install pyarmor"
}

# Check for PyInstaller/Auto-Py-To-Exe
if (Get-Command "pyinstaller" -ErrorAction SilentlyContinue) {
    Write-Host "PyInstaller found. Creating executable..."
    # pyinstaller --onefile src/payload/troyano.py
    Write-Host "Executable generation skipped (Uncomment in script to enable)."
} else {
    Write-Host "PyInstaller not found. Install it with: pip install pyinstaller"
}

Write-Host "Build steps completed."
