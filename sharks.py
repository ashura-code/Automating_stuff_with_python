import requests
import json
import bs4

data = []

i= 0

for j in range(1,15):
    req = requests.get('https://imgflip.com/memesearch?q=shark&page=1')

    soup = bs4.BeautifulSoup(req.text, 'html.parser')

    element = soup.select("img")




    for i in range(2,len(element)):
        # print("https:"+element[i].get('src'))
        data.append("https:"+element[i].get('src'))
        print(len(element))


print("done")
print(i)
print(len(data))



json_string = json.dumps({"results":data})

print(json_string)
