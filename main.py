import requests
from bs4 import BeautifulSoup

url = "https://www.goal.com/en-gb"
data = requests.get(url)

soup = BeautifulSoup(data.content, 'lxml')
content = soup.find_all("h3", limit=20)

for conti in content:
  print(f"{conti.a.text} \n https://www.goal.com/{conti.a['href']} \n")

