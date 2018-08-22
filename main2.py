import sys

import yaml
import speech_recognition as sr

from brain import brain
from GreyMatter.SenseCells.tts import tts

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

voice _file  = os.getcwd() + '/uploads/' + sys.argv[1]

def main(voice_file):
	r = sr.Recognizer()
	with sr.WavFile(voice_file) as source:
		audio = r.record(source)

	try :
		speech_text = r.recognize_google(audio).lower().replace("'","")
		print("Mercury thinks you siad'"+speech_text+"'")
	except sr.UnknownValueError:
		print("Mercury could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))

	play_music.mp3gen(music_path)

	brain(name,speech_text,music_path,city_name,city_code,proxy_username, proxy_password)

main(voice_file)

