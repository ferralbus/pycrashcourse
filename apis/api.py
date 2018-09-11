#{}

import requests
import json

url = 'https://api.github.com/search/repositories'

parameters = {
	'q':'language:solidity',
	'sort':'stars'
}

r = requests.get(url, params = parameters)

response_dict = r.json()

items = response_dict['items']

for repo_dict in items:
	print("\n"+repo_dict['name'])
	print(repo_dict['description'])
	print(repo_dict['stargazers_count'])
