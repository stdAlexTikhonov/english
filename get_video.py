import requests
from bs4 import BeautifulSoup

import urllib
import re
import sys
sys.stdout = open('file.txt', 'w')
text_file = open("source.txt", "w")




def get_data(item_url):
	f = urllib.request.urlopen(item_url)
	text_file.write(str(f.read()))
	
	
get_data('http://www.ted.com/talks/susan_cain_the_power_of_introverts')
text_file.close()

with open ("source.txt", "r") as myfile:
    data=myfile.readlines()
	
string = "".join(data)

pattern = r'high":"http://.+.mp4\?'
result = re.search(pattern, string)

print(result.group())

