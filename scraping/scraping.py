import requests
import json
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/name/nm0000138/?ref_=nv_sr_1'
page = requests.get(url)
print(page.status_code)
soup = BeautifulSoup(page.content,'html.parser')
person = json.loads(soup.find('script',type = 'application/ld+json').text)
print(person['name'] + ' was born on ' + person['birthDate'])
