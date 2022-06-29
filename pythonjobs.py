import requests
from bs4 import BeautifulSoup

url = "https://www.jobsite.co.uk/jobs/software-engineer/in-london"
data = requests.get(url)
soup = BeautifulSoup(data.content, 'lxml')
content = soup.find_all("header")
for conti in content:
  print(f"{conti}")