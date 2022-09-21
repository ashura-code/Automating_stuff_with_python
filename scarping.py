# import requests and bs4
# using requests get the url
# make a soup using the req in txt form and in 'html.parser'
# in that soup  , select the id / class / tag
# and use gettext with that value to get the answer

import requests

from bs4 import BeautifulSoup


req = requests.get("https://weather.com/en-IN/weather/today/l/12.98,79.17?par=google")
soup = BeautifulSoup(req.text, 'html.parser')



weather_element = soup.select('.CurrentConditions--tempValue--3a50n')
weather = weather_element[0].getText()

location_element = soup.select('.Card--cardHeading--5_qfE')
location = location_element[0].getText()


image_element = soup.select('section[style]')[0]

image_unparsed = (image_element.get('style'))
print(image_unparsed)






# print(image_element)

print(location)
print("The weather is "+weather+" C")







