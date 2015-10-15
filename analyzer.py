import os,sys
import numpy

from PIL import Image
from pprint import pprint

class Analyze():
    def __init__(self, img_dir):
        self.imlist = []
        self.getImages(img_dir)
        self.combine()

    def getImages(self, img_dir):
        # for img in self.filelist:
        #     self.imlist.append(Image.open(img_dir + img))
        allfiles=os.listdir(img_dir)
        self.imlist=[img_dir + filename for filename in allfiles if  filename[-4:] in [".jpg",".JPG"]]

    # see: https://stackoverflow.com/questions/17291455/how-to-get-an-average-picture-from-100-pictures-using-pil
    def combine(self):
        imlist=self.imlist
        pprint(imlist)
        # Assuming all images are the same size, get dimensions of first image
        w,h=Image.open(imlist[0]).size
        N=len(imlist)

        # Create a numpy array of floats to store the average (assume RGB images)
        arr=numpy.zeros((h,w,3),numpy.float)

        # Build up average pixel intensities, casting each image as an array of floats
        for im in imlist:
            imarr=numpy.array(Image.open(im),dtype=numpy.float)
            arr=arr+imarr/N

        # Round values in array and cast as 8-bit integer
        arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

        # Generate, save and preview final image
        out=Image.fromarray(arr,mode="RGB")
        out.save("Average.png")
        out.show()