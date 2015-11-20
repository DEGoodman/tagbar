import colorsys
import os,sys
import numpy

from PIL import Image, ImagePalette
from pprint import pprint

def compile():
    im = Image.open(os.getcwd() + '/app/static/images/Average.jpg') # hardcoded avg file
    w, h = im.size
    hist = im.histogram()
    arr=numpy.zeros((h,w,3),numpy.float)
    quantized = im.quantize(colors=5, kmeans=3)
    convert_rgb = quantized.convert('RGB')
    colors = convert_rgb.getcolors(w*h);
    main_colors = sorted(colors)[::-1] # reverse sort the list
    return main_colors
