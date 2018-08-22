#pip install selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from SenseCells.tts import tts

def open_firefox():
	tts('Aye aye captain, opening firefox')
	webdriver.Firefox()
	
def google_open(speech_text):
	words_of_message = speech_text.split()
	words_of_message.remove('google')
	cleaned_message = ' '.join(words_of_message)
	tts('Opening google')
	browser = webdriver.Firefox()
	#browser.maximize_window()
	browser.get('https://www.google.com')
	search = browser.find_element_by_name('q')
	search.send_keys(cleaned_message)
	search.send_keys(Keys.RETURN)
	#time.sleep(120)
	#browser.close()

def youtube_open(speech_text):
	words_of_message = speech_text.split()
	words_of_message.remove('youtube')
	cleaned_message = ' '.join(words_of_message)
	tts('Opening youtube')
	browser = webdriver.Firefox()
	#browser.maximize_window()
	browser.get('https://www.youtube.com')
	search = browser.find_element_by_name('search_query')
	search.send_keys(cleaned_message)
	search.send_keys(Keys.RETURN)
	#time.sleep(120)
	#browser.close()

def search_net(speech_text):
	browser = webdriver.Firefox()
	#browser.maximize_window()
	browser.get('https://www.google.com')
	search = browser.find_element_by_name('q')
	search.send_keys(speech_text)
	search.send_keys(Keys.RETURN)
	#time.sleep(120)
	#browser.close()

#google_open('google starwars')
