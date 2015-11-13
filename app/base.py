from analyzer import Analyze
import get_ig_photos
import process

import os
import sys

def main():
    ''' we already have some test images. Commenting out new downloads until this feature is finished.'''
    cur = os.getcwd()
    img_dir = cur + '/images/'
    process.compile(img_dir + "Average.jpg")


if  __name__ =='__main__':
    main()
