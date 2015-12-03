import json
import os
import re

from ast import literal_eval as make_tuple
from functools import partial
from json import JSONDecoder
from pprint import pprint

from .palletizer import Palletize

def make(data):
    f = open(os.getcwd() + '/app/static/css/colors.css', 'w')

    pos_base = ['a', 'b', 'c', 'd', 'e']
    num = 0
    # not sure why data is a nested list
    for quant,col  in data[0]:
        f.write('#%s' % pos_base[num])
        f.write(' {\n\tbackground-color: rgb') # nastiness
        f.write(str(col))
        f.write(';\n}\n\n')
        num += 1

    pos_comp = ['f', 'g', 'h', 'i', 'j']
    num = 0

    Palletize('%02x%02x%02x' % data[0][0][1])
    # newcols = comp_cols(data)
    f.close()
