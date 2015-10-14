from instagram.client import InstagramAPI
from pprint import pprint
import os
import requests
import sys
import urllib3

client_id = os.environ['tIG_CLIENT_ID'] # IG client id (env var)
client_secret = os.environ['tIG_CLIENT_SECRET'] # IG client secret (env var)

api = InstagramAPI(client_id=client_id, client_secret=client_secret)

tag_name=sys.argv[1]
pprint("looking for \'%s\'." % tag_name)
# return last 20 photos of tag
recent = api.tag_recent_media(30, 1000000000, tag_name)

# recent[0] is list of returned media
for media in recent[0]:
    pprint(media.images['standard_resolution'].url)
