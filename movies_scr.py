import requests
import bs4

req = requests.get('https://www.imdb.com/chart/top/')

soup = bs4.BeautifulSoup(req.text, 'html.parser')

element = soup.select('tbody')

print(element)
print("hai")






