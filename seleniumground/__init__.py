# It was a little tricky to download and import selenium
'''
   In the same venv  , create a new python  package
   in the python package go the pycharm dashboard in the top right corner

   and go to preferences > or use (cmd + ,) > the proeject > interpreter > click on the + icon and install selenium

'''


from selenium import webdriver  # this is the normal way to import selenium
from selenium.webdriver.common.keys import Keys    # importing the keyboard keys to use keyboard press actions (we use ENTER in this code)


# another problem came with the geckodriver package.
# downloaded the package from the venv current directory terminal using brew
# now it works perfectly.


browser = webdriver.Firefox()  # getting the webdriver for Firefox since i only had geckodriver installed , we can also use chromedriver but I didn't download it


# dont mind theese
# browser.get("http://inventwithpython.com")  # fetching the website
#
# elem = browser.find_elements_by_link_text('Read Online for Free')
#
#
#     browser.get("http://inventwithpython.com")
#     elem[i].click()



browser.get("https://auth.geeksforgeeks.org/?to=https://www.geeksforgeeks.org/")  # getting the website login page
user = "uirefvyfjjkaouixzy@tmmbt.com"   # gwtting the email address of the user
password = "098@gmail.Com"      # getting the password of the user


userElem = (browser.find_element_by_name('user'))  # finding the usename input box
userElem.click()   # clicking the input box
userElem.send_keys(user) # passing the username to the username box

passElem = (browser.find_element_by_name('pass'))  # finding the password input box
passElem.click()    # clicking the password input box
passElem.send_keys(password) # passing the password to the password box
passElem.send_keys(Keys.ENTER) # Clicking ENTER to signing in.


# loginElem = browser.find_element_by_link_text('Sign In')
# loginElem.click()
