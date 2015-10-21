from analyzer import Analyze
import get_ig_photos
import process

import os
import sys

def main():
    ''' we already have some test images. Commenting out new downloads until this feature is finished.'''
    # get_ig_photos.Setup()
    cur = os.getcwd()
    img_dir = cur + '/images/'
    img_loc = Analyze(img_dir)
    process.compile(img_dir + "Average.png")


if  __name__ =='__main__':
    main()