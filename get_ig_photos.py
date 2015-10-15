from instagram.client import InstagramAPI
from pprint import pprint
import os
import requests
import sys
import urllib

class Setup:
    def __init__(self):
        self.client_id = os.environ['tIG_CLIENT_ID'] # IG client id (env var)
        self.client_secret = os.environ['tIG_CLIENT_SECRET'] # IG client secret (env var)
        self.api = InstagramAPI(client_id=self.client_id, client_secret=self.client_secret)

        #system vars
        self.cur = os.getcwd()
        self.images = self.cur + '/images/'
        self.housekeeping()
        self.tag_name=sys.argv[1]
        pprint("looking for \'%s\'..." % self.tag_name)
        # return last 20 photos of tag
        self.recent = self.api.tag_recent_media(20, 1000000000, self.tag_name)
        # recent[0] is list of returned media
        for media in self.recent[0]:
            self.keep(media.images['standard_resolution'].url)
        pprint("Downloaded %s images" % len(self.recent[0]))

        # pass back our images dir so we don't have to keep querying it
        return self.images

    def housekeeping(self):
        filelist = [ f for f in os.listdir(self.images + ".") if f.endswith(".jpg") ]
        pprint("Removing old image files.")
        for f in filelist:
            os.remove(self.images + f)

    def keep(self, img):
        name = str(img)[-20:]
        # create new file for img
        with open(self.images + name, 'w'):
            urllib.urlretrieve(img, self.images + name)

   