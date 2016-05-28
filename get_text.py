import requests
from bs4 import BeautifulSoup
import sys

sys.stdout = open( "source.txt", "w+" )

def get_data(item_url):
	source_code = requests.get(item_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for item_name in soup.findAll('span', {'class': 'talk-transcript__fragment'}):
		itog = item_name
		try:
			print(itog, "//")
			#print("'"+itog.string+"'")
		except:
			print(' error ');
	#for link in soup.findAll('a'):
		#href = link.get('href')
		#print(href)
		
get_data('http://www.ted.com/talks/susan_cain_the_power_of_introverts/transcript?language=en')