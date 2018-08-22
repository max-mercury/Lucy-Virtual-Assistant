from gtts import gTTS
import os
import sys

def tts(message):
    '''
    This function takes a message as an argument and converts it to speech depending on the OS

    #print(sys.platform)
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak'
        return os.system(tts_engine + ' "' + message + '"')
    '''
    tts = gTTS(text=message,lang='en')
    tts.save("good.mp3");
    os.system("mpg321 good.mp3")
