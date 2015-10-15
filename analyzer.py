import os
import sys

from pprint import pprint

class Analyze():
    def __init__(self, img_dir):
        self.filelist = [ f for f in os.listdir(img_dir + ".") if f.endswith(".jpg") ]
        pprint(self.filelist)