import requests
from bs4 import BeautifulSoup
import sys

sys.stdout = open( "rus.txt", "w+" )

def get_data(item_url):
	source_code = requests.get(item_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for item_name in soup.findAll('span', {'class': 'talk-transcript__fragment'}):
		itog = item_name
		try:
			#print(itog, "//")
			print("'"+itog.string+"'")
		except:
			print(' error ');
	#for link in soup.findAll('a'):
		#href = link.get('href')
		#print(href)
		
get_data('http://www.ted.com/talks/david_kwong_two_nerdy_obsessions_meet_and_it_s_magic/transcript?language=ru')