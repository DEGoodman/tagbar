from bs4 import BeautifulSoup
import os
import selenium.webdriver as webdriver
import requests

# access_token = # add IG access token
client_id = os.environ['tIG_CLIENT_ID'] # IG client id (env var)
INSTAGRAM_API = 'https://api.instagram.com/v1/'
# call_IG(tag="tucson")

def call_IG(tag="nofilter"):
    # ugly string concat for 'recent' results of provided tag.
    url = INSTAGRAM_API + 'tags/' + tag + "/media/recent?client_id=" + client_id
    driver = webdriver.Firefox()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source)

    for x in soup.findAll('li', {'class':'photo'}):
        print x

call_IG(tag="tucson")