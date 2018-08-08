'''
###################
# swearjar        #
#        v1.9-5   #
#                 #
#       by rudy   #
###################
'''


#Gotta import these modules to make stuff work
#Shoutout to the Python community for making this stuff
import speech_recognition as sr
import os
import pyaudio
from texttable import Texttable


#This method is called to draw the pretty table that displays the program
def update_status(status_text):
    os.system('cls')
    the_rows = [["Swear-Jar Counter","v1.9-5"],["Selected Device",selected_device],["Total Words", total_words],["Swears Per Word", swears_per_word],["Swear Count", swear_count],["Most Recent Text", most_recent_record],[" "," "],[" "," "],["Stats", status_text],["Press CTRL+C to Exit",""]]
    t = Texttable()
    t.add_rows(the_rows)
    print(t.draw())


#Initialize variables
r = sr.Recognizer()
swear_count = 0
total_words = 0
swears_per_word = 0
most_recent_record = ''
selected_device = ''
swears = ['fuck', 'shit', 'damn', 'ass', 'bitch', 'hell'] #note to self: find a more exhaustive swear list online
                                                                #multiple languages?

#Print a list of the detected microphones on the system
os.system('cls')
print("Here are your audio devices:\n\n")
num_devices = len(sr.Microphone.list_microphone_names())
mic_rows = [["Number","Audio Device"]]
for i in range(0,num_devices):
    mic_rows.append([str(i),sr.Microphone.list_microphone_names()[i]])

t = Texttable()
t.add_rows(mic_rows)
print(t.draw())


#Ask user to select a microphone
mic_choice = int(input("Which microphone would you like to count swears from? (Use the numbers 0-" + str(num_devices-1) + ")\n\n>>")) #subtract 1 cause zero-indexed list of devices
selected_device = sr.Microphone.list_microphone_names()[mic_choice]


#This loop keeps our program going for perpetuity until the user closes it
#The program loops in ~5 second intervals, listening to the microphone for 5 seconds, and then counting the swears
while True:
    try:
        #Instantiate the user's selected microphone
        m = sr.Microphone(device_index=mic_choice)
        with m as source:
            update_status("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5) #adjust for ambient noise for 0.5 seconds
            
            #Listen to the microphone for 5 seconds
            audio = r.listen(source,phrase_time_limit=5)
            try:
                update_status("Speech Detected...")
                
                #Use Google API to convert audio to text
                this_record = r.recognize_google(audio)
                most_recent_record = this_record #update the value to be displayed
                
                #Split recorded text into array of strings
                record_words = this_record.split()
                total_words += len(record_words) #update the value to be displayed
                swears_per_word = swear_count/total_words
                
                #Update
                update_status("Success!!")
                
                #Check each word to see if it's a swear or has an asterisk -- Google API uses asterisks to censor detected swears
                for a_word in record_words:
                    if a_word in swears or "*" in a_word:
                        #Update the values to be displayed
                        swear_count+=1
                        update_status("Swear Detected!!  ")
            except sr.UnknownValueError:
                #API could not discern what was said
                update_status("Could not understand")
            except sr.RequestError as e:
                #API did not answer our request
                update_status("Error: {0}".format(e))
    except OSError as err:
        #Issue with Audio Device selection, user is re-prompted with the selection menu
        
        #Print a list of the detected microphones on the system
        os.system('cls')
        print("Here are your audio devices:\n\n")
        num_devices = len(sr.Microphone.list_microphone_names())
        mic_rows = [["Number","Audio Device"]]
        for i in range(0,num_devices):
            mic_rows.append([str(i),sr.Microphone.list_microphone_names()[i]])

        t = Texttable()
        t.add_rows(mic_rows)
        print(t.draw())
        print("You've selected an output device instead of an input device; try a different device.")

        #Ask user to select a microphone
        mic_choice = int(input("Which microphone would you like to count swears from? (Use the numbers 0-" + str(num_devices-1) + ")\n\n>>")) #subtract 1 cause zero-indexed list of devices
        selected_device = sr.Microphone.list_microphone_names()[mic_choice]
        print("You've selected: " + selected_device + "\n\n") #print our chosen mic's name