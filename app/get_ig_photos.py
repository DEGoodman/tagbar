from instagram.client import InstagramAPI
from pprint import pprint
from ConfigParser import SafeConfigParser
import os
import requests
import sys
import urllib

class Setup:
    def __init__(self, tag_name):
        #system vars
        self.cur = os.getcwd()

        # import keys
        config = SafeConfigParser()
        config.read(self.cur + '/app/settings.ini')
        client_id = config.get('Instagram', 'client_id') # IG client id (settings.ini)
        client_secret = config.get('Instagram', 'client_secret') # IG client secret (^)
        self.api = InstagramAPI(client_id=client_id, client_secret=client_secret)

        self.images = self.cur + '/app/static/images/'
        self.housekeeping()
        self.tag_name=tag_name
        pprint("looking for \'%s\'..." % self.tag_name)
        # download 5, but only one image is used at a time
        self.recent = self.api.tag_recent_media(5, 1000000000, self.tag_name)
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
