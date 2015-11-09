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

    # split into red, green, blue
    r = hist[0:256]
    g = hist[256:256*2]
    b = hist[256*2: 256*3]

    rgb_vals = {
        'r': sum( i*w for i, w in enumerate(r) ) / sum(r),
        'g': sum( i*w for i, w in enumerate(g) ) / sum(g),
        'b': sum( i*w for i, w in enumerate(b) ) / sum(b)
    }
    pprint(rgb_vals)
    # hsv_vals = colorsys.rgb_to_hsv(rgb_vals['r'], rgb_vals['g'], rgb_vals['b'])
    # pprint(hsv_vals)

    # # value adjustments
    # hsv = {}
    # # hue will stay the same
    # hsv['h'] = hsv_vals[0] * 360
    # # saturation will increase to a reasonable number
    # hsv['s'] = 80
    # # brightness
    # hsv['v'] = 80
    # pprint(hsv)
    #
    quantized = im.quantize(colors=5, kmeans=3)
    convert_rgb = quantized.convert('RGB')
    colors = convert_rgb.getcolors(w*h);
    main_colors = sorted(colors)[::-1] # reverse sort the list
    print(main_colors)
    return main_colors
