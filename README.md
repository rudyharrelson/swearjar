# SwearJar
This program listens to a microphone and counts utterances of swears. Currently, the program is only supported on [Windows](https://www.microsoft.com/en-us/windows) systems. Requires an [Internet connection](https://simple.wikipedia.org/wiki/Internet) to function, as it relies on the [Google Web Speech API](https://www.google.com/chrome/demos/speech.html) to translate audio to text. SwearJar is written in [Python 3](https://www.python.org/downloads/), and compiled to C using [PyInstaller](https://www.pyinstaller.org/).

+ <span style="font-size:small">**Note:** Your swear count will restart every time you close the program! This will be fixed in the upcoming 2.0 patch.</span>
+ <span style="font-size:small">**Note:** The Google API may impose limitations on the number of calls the program can make a day, so it may stop working at times due to API limitations being enforced. </span>

## How To Use
Through the mystical powers of science, we are able to compile the Python program and all its requisite code libraries into a single executable file for Windows. You can find the latest version at [/bin/SwearJar.exe](https://github.com/rudyharrelson/SwearJar/raw/master/bin/SwearJar.exe). Just run 'SwearJar.exe' and you're done!
![](https://i.imgur.com/jzR0lHd.png)

### Uninstalling
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

### Cloning the Source Code from Git
You can clone the source code 

### Compiling with PyInstaller

Now, open the command prompt (preferably in Administrator mode) in the same directory as "compile.bat" and run the command:
```compile.bat```
![]()

### Demo
Once you run ```python SwearJar.py```, you'll be given the option to select your Microphone device:
![](https://i.imgur.com/CvCTikI.png)

Enter a number to select your Microphone. Then the program will begin listening and counting the swears:
![](https://i.imgur.com/Ftu5ENl.png)
