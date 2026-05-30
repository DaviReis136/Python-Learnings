#Retrieving data from a web page using import JSON.

import urllib.request
import json

url = input('Enter location: ')

if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving', url)

data = urllib.request.urlopen(url).read()

print('Retrieved',len(data),'characters')

info = json.loads(data)

counts = []

for item in info['comments']:
    counts.append(item['count'])

print('Count:', len(counts))
print('Sum:', sum(counts))
