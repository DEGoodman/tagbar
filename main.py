from pprint import pprint
import os
import requests
import sys
import urllib3
# access_token = # add IG access token
client_id = os.environ['tIG_CLIENT_ID'] # IG client id (env var)
INSTAGRAM_API = 'https://api.instagram.com/v1/'

def build_url(tag="nofilter"):
    # ugly string concat for 'recent' results of provided tag.
    return INSTAGRAM_API + 'tags/' + tag + "/media/recent?client_id=" + client_id

def get_img(url):
    r = requests.get(url)
    # this is hopefully a 200
    print(r.status_code)
    # Let's see what we get back!
    print(r.text)


def get_links(url):
    j = requests.get(url).json() # jsonify tag API query
    return [obj["link"] for obj in j["data"]] # get all links from ^

# for flexibility
def get_storage(static="static/"):
    return static

#enter a tab when calling the program
raw_url = build_url(tag=sys.argv[1])
print("looking for \'%s\'." % sys.argv[1])
links = get_links(raw_url)
print(links)
path = get_storage()

# let's get our photos
# onlu one for now to save on request #'s
img = get_img(links[0])
# TODO: 
# for p in links:
#     img = get_img(p)


