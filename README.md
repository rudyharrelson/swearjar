# Swear Jar
This program listens to a microphone and counts utterances of swears. Currently, the program is only supported on [Windows](https://www.microsoft.com/en-us/windows) systems. Requires an [Internet connection](https://simple.wikipedia.org/wiki/Internet) to function, as it relies on the [Google Web Speech API](https://www.google.com/chrome/demos/speech.html) to translate audio to text. SwearJar is written in [Python 3](https://www.python.org/downloads/), and compiled to C using [PyInstaller](https://www.pyinstaller.org/)

## Single-File Executable (AKA "Normal Mode")
Through the mystical powers of science, we are able to compile the Python program and all its requisite code libraries into a single executable file for Windows. You can find the latest version at [/bin/swearjar.exe](https://github.com/rudyharrelson/swearjar/raw/master/bin/swearjar.exe). Just run 'swearjar.exe' and you're done!
![](https://i.imgur.com/jzR0lHd.png)

## Advanced Mode (AKA "Unnecessarily Difficult Mode")
### Install Python 
First you'll need to install [Python 3](https://www.python.org/downloads/). Any version past 3.7.0 will do. 

When installing Python 3, make sure "pip" is selected to be installed under "Optional Features"
![](https://i.imgur.com/NhE3hKR.png)

After installing Python, open the command-prompt in Windows and enter:

```pip install SpeechRecognition pyaudio texttable```

This command should download and install the necessary modules to run this program. 

Once these are installed, open the command prompt in the same directory as swearjar.py:
![](https://i.imgur.com/FfEtSCk.png)

Then run the command:
```python swearjar.py```


![](https://i.imgur.com/UUniG6E.png)

### Demo
Once you run ```python swearjar.py```, you'll be given the option to select your Microphone device:
![](https://i.imgur.com/CvCTikI.png)

Enter a number to select your Microphone. Then the program will begin listening and counting the swears:
![](https://i.imgur.com/Ftu5ENl.png)
