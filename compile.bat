python -O -m PyInstaller --onefile --icon=app.ico --distpath ./bin --specpath ./temp --workpath ./temp swearjar.py

echo y|rmdir /s temp

echo y|rmdir /s __pycache__