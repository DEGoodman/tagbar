import analyzer
import get_ig_photos

import os
import sys

def main():
    ''' we already have some test images. Commenting out new downloads until this feature is finished.'''
    get_ig_photos.Setup()
    cur = os.getcwd()
    img_dir = cur + '/images/'
    analyzer.Analyze(img_dir)

if  __name__ =='__main__':
    main()