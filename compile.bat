python -B -O -m PyInstaller --onefile --icon=./media/app.ico --distpath ./bin --specpath ./temp --workpath ./temp ./src/swearjar.py

echo y|rmdir /s temp