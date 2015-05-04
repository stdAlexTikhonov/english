import requests
from bs4 import BeautifulSoup

import urllib
import re
import sys

text_file = open("source.txt", "w")




def get_data(item_url):
	f = urllib.request.urlopen(item_url)
	text_file.write(str(f.read()))
	
	
get_data('http://www.ted.com/talks/bill_gates')
text_file.close()

with open ("source.txt", "r") as myfile:
    data=myfile.readlines()
	
string = "".join(data)

pattern = r'high":"http://.+.mp4\?'
result = re.search(pattern, string)

print(result.group())

