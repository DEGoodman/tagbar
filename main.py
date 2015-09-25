from pprint import pprint
import os
import requests

# access_token = # add IG access token
client_id = os.environ['tIG_CLIENT_ID'] # IG client id (env var)
INSTAGRAM_API = 'https://api.instagram.com/v1/'

def build_url(tag="nofilter"):
    # ugly string concat for 'recent' results of provided tag.
    return INSTAGRAM_API + 'tags/' + tag + "/media/recent?client_id=" + client_id

def get_links(url):
    j = requests.get(url).json() # jsonify tag API query
    return [obj["link"] for obj in j["data"]] # get all links from ^

# for flexibility
def get_storage(default="static/"):
    return default

raw_url = build_url(tag="tucson")
links = get_links(raw_url)
print(links)
path = get_storage()