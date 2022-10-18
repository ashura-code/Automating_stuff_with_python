
import requests   # to get the html of the webpage
import bs4        # to regx from the html
import shutil     # to download the image and store it in the folder


# getting the image link
i = 1002    # a random number of the comic (you can loop this number to get more comics)
res = requests.get(f'https://xkcd.com/{i}/')   # requesting html to xkcd comics
soup = bs4.BeautifulSoup(res.text, 'html.parser')  # Converting request element to soup element
element = soup.select('#comic img')   # from the soup element , selecting the element that has the link of the comic
link = "https:" + (element[0].get('src'))  # the acquired link element gives us the link without the https: at the front so we are adding it ourselves.
print(link)  # printing the final image link.


# Downloading the image
file_name = element[0].get('alt')  # to have a file name , we are using bs4 to get the title of the comic.
req = requests.get(link,stream=True)  # Using requests to check if the link is valid and to get the raw form of the comic.


if res.status_code == 200: # if the link is valid we go ahead to download the comic
    with open(file_name, 'wb') as f:  # using file operations to crate a file with the name of the comic
        shutil.copyfileobj(req.raw, f)  # using shutil to write the comic image(which is gotten using requests in the 17th line) to the created file
    print('Image sucessfully Downloaded: ', file_name)
else:
    print("Image couldn't be downloaded")