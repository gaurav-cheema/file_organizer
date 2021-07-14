import requests
from bs4 import BeautifulSoup

URL = "https://www.computerhope.com/issues/ch001789.htm"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

b_tags = soup.findAll("b")

tags = []
for tag in b_tags:
    tags.append(tag.text)

textFile = open("ext_list.txt", "w")

for tag in tags:
    textFile.write(tag + "\n")
textFile.close()
