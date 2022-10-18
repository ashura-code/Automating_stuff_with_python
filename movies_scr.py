import requests
import bs4

req = requests.get('http://127.0.0.1:5500/ok.html')

soup = bs4.BeautifulSoup(req.text, 'html.parser')

element = soup.select('h1')

print(element)






