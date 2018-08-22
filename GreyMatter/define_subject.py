#pip install wikipedia
import re

import wikipedia

from SenseCells.tts import tts

def define_subject(speech_text):
	words_of_message = speech_text.split()
	words_of_message.remove('define')
	cleaned_message = ' '.join(words_of_message)
	
	try : 
		wiki_data = wikipedia.summary(cleaned_message, sentences=5)

		regEx = re.compile(r'([^\(]*)\([^\)]*\) *(.*)')
		m = regEx.match(wiki_data)
		while m:	
			wiki_data = m.group(1) + m.group(2)
			m = regEx.match(wiki_data)

		wiki_data = wiki_data.replace("'","")
		wiki_data = wiki_data.encode('ascii','ignore')
		r_data =  wiki_data.split('.')
		t_data = r_data[0] + r_data[1]
		print t_data
		tts(t_data)
		

	except wikipedia.exceptions.DisambiguationError as e:
		tts('Can you please be more specific? You may choose something from the following.')
		print("Can you please be more specific? You may choose something from the following.;{0}".format(e))