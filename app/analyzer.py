import os,sys
import numpy
import random

from collections import Counter
from PIL import Image
from pprint import pprint

class Analyze():
    def __init__(self):
        self.cur = os.getcwd()
        self.img_dir = self.cur + '/app/static/images/'
        self.imlist = []

    def getImages(self):
        # for img in self.filelist:
        #     self.imlist.append(Image.open(img_dir + img))
        allfiles=os.listdir(self.img_dir)
        self.imlist=[self.img_dir + filename for filename in allfiles if  filename[-4:] in [".jpg",".JPG"]]

    # see: https://stackoverflow.com/questions/17291455/how-to-get-an-average-picture-from-100-pictures-using-pil
    def combine(self):
        im = random.choice(self.imlist)
        # Assuming all images are the same size, get dimensions of first image
        w,h=Image.open(im).size
        N=len(im)

        # Create a numpy array of floats to store the average (assume RGB images)
        arr=numpy.zeros((h,w,3),numpy.float)

        # Build up average pixel intensities, casting each image as an array of floats
        imarr=numpy.array(Image.open(im),dtype=numpy.float)

        # Round values in array and cast as 8-bit integer
        arr=numpy.array(numpy.round(imarr),dtype=numpy.uint8)

        # Generate, save and preview final image
        out=Image.fromarray(arr,mode="RGB")
        out.save(self.img_dir + "Average.jpg")
