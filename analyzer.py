import os,sys
import numpy

from PIL import Image
from pprint import pprint

class Analyze():
    def __init__(self, img_dir):
        self.filelist = [ f for f in os.listdir(img_dir + ".") if f.endswith(".jpg") ]
        self.imagelist = []
        self.getImages(img_dir)
        self.combine()

    def getImages(self, img_dir):
        for img in self.filelist:
            self.imagelist.append(Image.open(img_dir + img))
            # print(img_dir + img)

    def combine(self):
        pprint(self.imagelist)
