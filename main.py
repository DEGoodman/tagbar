from bs4 import BeautifulSoup
from pprint import pprint
import json
import os
import requests
import ruamel.yaml as yaml

# access_token = # add IG access token
client_id = os.environ['tIG_CLIENT_ID'] # IG client id (env var)
INSTAGRAM_API = 'https://api.instagram.com/v1/'

def build_url(tag="nofilter"):
    # ugly string concat for 'recent' results of provided tag.
    return INSTAGRAM_API + 'tags/' + tag + "/media/recent?client_id=" + client_id

def get_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    # pprint(soup)
    # j = json.loads(str(soup))
    # pprint(j)
    y = yaml.load(str(soup))
    pprint(y)
    pprint(y['link'])

raw_url = build_url(tag="tucson")
page = get_page(raw_url)
