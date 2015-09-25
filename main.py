from bs4 import BeautifulSoup
import json
import os
from pprint import pprint
import selenium.webdriver as webdriver
# import simplejson as json
import requests
import urllib2

# access_token = # add IG access token
client_id = os.environ['tIG_CLIENT_ID'] # IG client id (env var)
INSTAGRAM_API = 'https://api.instagram.com/v1/'
# call_IG(tag="tucson")

def call_IG(tag="nofilter"):
    # ugly string concat for 'recent' results of provided tag.
    raw_url = INSTAGRAM_API + 'tags/' + tag + "/media/recent?client_id=" + client_id
    soup = BeautifulSoup(urllib2.urlopen(raw_url).read(), "html.parser")

    results = soup.findAll("link")
    pprint(results)
    # dict=json.loads(str(soup))
    # pprint(dict)
    # links = dict["u'link'"]
    # pprint(links)
    # for x in soup.findAll('link'):
    #     print x

call_IG(tag="tucson")