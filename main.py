import snowboydecoder
import sys
import signal
import yaml
import speech_recognition as sr

from brain import brain
from GreyMatter.SenseCells.tts import tts
from GreyMatter import play_music

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

#Functioning Variables
name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']
proxy_username = profile_data['proxy_username']
proxy_password = profile_data['proxy_password']
music_path = profile_data['music_path']

play_music.mp3gen(music_path)


tts('Welcome,systems are now ready to run. How can I help you?')

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted


def main():
    # Main Function
    r = sr.Recognizer()
    with sr.Microphone() as source:#device_index=1
        r.adjust_for_ambient_noise(source)  # here
        print("Say Something!")
        audio = r.listen(source)

    try:
        speech_text = r.recognize_google(audio).lower().replace("'","")
        print("Lucy thinks you said '" + speech_text + "'")
        #Calls Brain Function
        brain(name,speech_text,music_path,city_name,city_code,proxy_username,proxy_password)
    except sr.UnknownValueError:
        print("Lucy could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognitionservice;{0}".format(e))



if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

detector.start(detected_callback=main,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()

