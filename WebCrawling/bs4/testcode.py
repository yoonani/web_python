import requests
from bs4 import BeautifulSoup

url = 'http://ydct.or.kr/projects/?sf_paged='
response = requests.get( url + "1" )

titles = []
descs = []
dates = []


html = response.text
soup = BeautifulSoup(html, 'html.parser')
titleBoxes = soup.find_all('div', class_='item-title-box')
for i in titleBoxes:
    print( i.select_one(".item-title").text )