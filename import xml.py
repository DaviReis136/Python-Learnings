import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
contador = 0
sum_tot = 0
soma = []

for result in counts:
    counts = tree.findall('.//count')
    nums.append(str(result.text))
    print(result.text)

for item in nums: 
    sum_tot += int(item) 

print('Count:', len(nums))
print('Sum:', sum_tot )

#http://py4e-data.dr-chuck.net/comments_2376855.xml
#http://py4e-data.dr-chuck.net/comments_42.xml