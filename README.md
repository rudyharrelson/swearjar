# SwearJar
This program listens to a microphone and counts utterances of swears. Currently, the program is only supported on [Windows](https://www.microsoft.com/en-us/windows) systems. Requires an [Internet connection](https://simple.wikipedia.org/wiki/Internet) to function, as it relies on the [Google Web Speech API](https://www.google.com/chrome/demos/speech.html) to translate audio to text. SwearJar is written in [Python 3](https://www.python.org/downloads/), and compiled to C using [PyInstaller](https://www.pyinstaller.org/).

+ <span style="font-size:small">**Note:** Your swear count will restart every time you close the program! This will be fixed in the upcoming 2.0 patch.</span>
+ <span style="font-size:small">**Note:** The Google API may impose limitations on the number of calls the program can make a day, so it may stop working at times due to API limitations being enforced. </span>

## How To Use
Through the mystical powers of science, we are able to compile the Python program and all its requisite code libraries into a single executable file for Windows. You can find the latest version at [/bin/SwearJar.exe](https://github.com/rudyharrelson/SwearJar/raw/master/bin/SwearJar.exe). When you run "SwearJar.exe", you'll be prompted to select your microphone. After that, the program will begin listening for swears. 
![](https://i.imgur.com/jzR0lHd.png)

### For Streamers
Need a text file so your streaming software can display the swear count on your overlay? No problem. The current swear count is exported to "swearcount.txt". 

## Uninstalling
Tired of measuring the rapid decay of your already lacking vocabulary? You can uninstall SwearJar by simply deleting the 'SwearJar.exe' file. 

![](https://i.imgur.com/5lQ5VQc.png)

## Compile It Yourself (AKA "Unnecessarily Difficult Mode")
### Install Python
First you'll need to install [Python 3](https://www.python.org/downloads/). Any version past 3.6.0 will do. 

When installing Python 3, make sure "pip" is selected to be installed under "Optional Features"
![](https://i.imgur.com/NhE3hKR.png)

### Install Modules
After installing Python, open the command-prompt in Windows (preferably in Administrator mode) and enter:

```pip install PyInstaller SpeechRecognition pyaudio texttable```

This command should download and install the modules that compiling the source code relies on. 

### Install Git
We need to install a program called [Git](https://git-scm.com/download/win) to clone the source code available on this GitHub page.

### Clone Source Code via Git
You can download the source code by cloning the repository in git:

```git clone https://github.com/rudyharrelson/swearjar```

![](https://i.imgur.com/em6TLX3.png)

### Compiling with PyInstaller

Now, open the command prompt (preferably in Administrator mode) in the same directory as "compile.bat" and run the command:

```compile.bat```

The "compile.bat" file runs the following command:

```
python -O -m PyInstaller --onefile --icon=./media/app.ico --distpath ./bin --specpath ./temp --workpath ./temp ./src/swearjar.py

echo y|rmdir /s temp

echo y|rmdir /s src\__pycache__
```
The above command just invokes the compiler via PyInstaller. This process creates 2 temp folders, and the batch file deletes them after the .exe file has been compiled.
![](https://i.imgur.com/tuqUuSo.png)

After the batch file is through running, you can find "swearjar.exe" in the /bin/ folder. 
