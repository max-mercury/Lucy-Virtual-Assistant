#pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from SenseCells.tts import tts

	
def faculty_search(speech_text):
	words_of_message = speech_text.split()
	words_of_message.remove('faculty')
	cleaned_message = ' '.join(words_of_message)
	name = cleaned_message.split()
	f_name = name[0]
	lname = name[1]
	tts('Searching for Faculty')
	browser = webdriver.Firefox()
	link = 'http://vit.edu.in/faculty/' + f_name + '-' + lname
	browser.get(link)
	search = browser.find_element_by_name('q')
	search.send_keys(cleaned_message)
	search.send_keys(Keys.RETURN)

def about_vit():
	tts('Information About V I T')
	browser = webdriver.Firefox()
	link = 'https://en.wikipedia.org/wiki/Vidyalankar_Institute_of_Technology'
	browser.get(link)
	#browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

