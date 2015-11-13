from instagram.client import InstagramAPI
from pprint import pprint
import os
import requests
import sys
import urllib

class Setup:
    def __init__(self, tag_name):
        self.client_id = os.environ['tIG_CLIENT_ID'] # IG client id (env var)
        self.client_secret = os.environ['tIG_CLIENT_SECRET'] # IG client secret (env var)
        self.api = InstagramAPI(client_id=self.client_id, client_secret=self.client_secret)

        #system vars
        self.cur = os.getcwd()
        self.images = self.cur + '/app/static/images/'
        self.housekeeping()
        self.tag_name=tag_name
        pprint("looking for \'%s\'..." % self.tag_name)
        # return last photo of tag
        # this is because the colrs turn out better
        self.recent = self.api.tag_recent_media(1, 1000000000, self.tag_name)
        # recent[0] is list of returned media
        for media in self.recent[0]:
            self.keep(media.images['standard_resolution'].url)
        pprint("Downloaded %s images" % len(self.recent[0]))

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
