import requests
from bs4 import BeautifulSoup

url = "https://www.thisisanfield.com/"
data = requests.get(url)
soup = BeautifulSoup(data.content, 'lxml')
content = soup.find_all("h3", class_="entry-title", limit=5)
for conti in content:
  print(f"{conti.text} \n {conti.a['href']} \n")