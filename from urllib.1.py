import urllib.request
from bs4 import BeautifulSoup

# Input values
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Repeat the process count + 1 times
for i in range(count):
    print("Retrieving:", url)

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    # Find all anchor tags
    tags = soup('a')

    # Get the link at the required position
    target = tags[position - 1]
    url = target.get('href')

    # Save the last name found
    last_name = target.text

print("Last name:", last_name)