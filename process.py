import os,sys
import numpy

from PIL import Image
from pprint import pprint

def compile(img):
    im = Image.open(img)
    w, h = im.size
    hist = im.histogram()
    pprint("w: %s, h: %s" % (w,h))
    arr=numpy.zeros((h,w,3),numpy.float)

    # split into red, green, blue
    r = hist[0:256]
    g = hist[256:256*2]
    b = hist[256*2: 256*3]

    # perform the weighted average of each channel:
    # the *index* is the channel value, and the *value* is its weight
    vals = {
        'r': sum( i*w for i, w in enumerate(r) ) / sum(r),
        'g': sum( i*w for i, w in enumerate(g) ) / sum(g),
        'b': sum( i*w for i, w in enumerate(b) ) / sum(b)
    }

    pprint(vals)
    arrvals = []
    out = Image.new("RGB", (612,612), (vals['r'], vals['g'], vals['b']))
    out.show()

