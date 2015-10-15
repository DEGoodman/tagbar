from instagram.client import InstagramAPI
from pprint import pprint
import os
import requests
import sys
import urllib
import urllib2
import urllib3

client_id = os.environ['tIG_CLIENT_ID'] # IG client id (env var)
client_secret = os.environ['tIG_CLIENT_SECRET'] # IG client secret (env var)
api = InstagramAPI(client_id=client_id, client_secret=client_secret)

#system vars
cur = os.getcwd()
images = cur + '/images/'

def housekeeping():
    filelist = [ f for f in os.listdir(images + ".") if f.endswith(".jpg")]
    pprint("Removing old image files.")
    for f in filelist:
        os.remove(images + f)

def keep(img):
    name = str(img)[-20:]
    # create new file for img
    f = open(images + name, 'w')
    urllib.urlretrieve(img, images + name)
    f.close()

housekeeping()
tag_name=sys.argv[1]
pprint("looking for \'%s\'..." % tag_name)

# return last 20 photos of tag
recent = api.tag_recent_media(20, 1000000000, tag_name)

# recent[0] is list of returned media
for media in recent[0]:
    keep(media.images['standard_resolution'].url)
pprint("Downloaded %s images" % len(recent[0]))

