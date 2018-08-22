#pip install requests and beautifulsoup4

import requests
from bs4 import BeautifulSoup

from SenseCells.tts import tts

#NDTV News
fixed_url = 'https://www.ndtv.com/latest'
news_headlines_list = []
news_details_list = []

for i in range (1,2):
	changing_slug = '/page-' + str(i)
	url = fixed_url + changing_slug
	r = requests.get(url)
	data = r.text

	soup = BeautifulSoup(data, "html.parser")

	for news_headlines in soup.findAll("div", {"class": "nstory_header"}):
		news_headlines_list.append(news_headlines.get_text())

	del news_headlines_list[-2:]

	for news_details in soup.findAll("div", {"class": "nstory_intro"}):
		news_details_list.append(news_details.get_text())

news_headlines_list_small = [element.lower().replace("(","").replace(")","").replace("'","").replace('\n','').replace(",","") for element in news_headlines_list]

news_details_list_small = [element.lower().replace("(","").replace(")","").replace("'","").replace('\n','').replace(",","")  for element in news_details_list]

news_dictonary = dict(zip(news_headlines_list_small, news_details_list_small))



def news_reader():
	#print news_headlines_list_small
	for key,value in news_dictonary.items():
		tts('Headline,' + key)
		tts('News,'+ value)
