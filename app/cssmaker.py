import json
import os
import re

from pprint import pprint

def make(data):
    f = open(os.getcwd() + '/app/static/css/colors.css', 'w')
    f.write('.color-swatches {\n\tmargin: 5px 0px -5px 0px;\n\twidth:550px;\n\toverflow:hidden;\n}\n')
    f.write('.color-swatch {\n\tfloat: left;\n\tmargin: 0px 5px;\n\tborder-radius: 3px;\n\twidth: 100px;\n\theight: 100px;\n}\n')

    pos_base = ['a', 'b', 'c', 'd', 'e']
    num = 0
    # not sure why data is a nested list
    for quant,col  in data[0]:
        f.write('#%s' % pos_base[num])
        f.write(' {\n\tbackground-color: rgb') # nastiness
        f.write(str(col))
        f.write(';\n}\n\n')
        num += 1

    # hex converter
    prim = data[0][0][1]
    hcol = '%02x%02x%02x' % prim
    # primstr = cols[8:28]
    # primtrim = str(re.findall("\([^\(\r\n\)]*\)", primstr))
    # primtup = tuple(int(v) for v in re.findall("[0-9]+", primtrim))
    # hcol = '%02x%02x%02x' % primtup
    with open(os.getcwd() + '/app/static/pallete.json') as j:
        print("we opened a json file!")

    pos_comp = ['f', 'g', 'h', 'i', 'j']
    num = 0
    newcols = comp_cols(data)

    f.close()

def comp_cols(data):
    pass
