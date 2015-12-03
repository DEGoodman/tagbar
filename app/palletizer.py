import os
import json

from functools import partial
from pprint import pprint

def Palletize(base):
    rgb = hex_to_rgb(base)
    print("Palletizer base rgb: ")
    print(rgb)
    jfile = open(os.getcwd() + '/app/static/pallete.json', 'r')
    rgb_from_json = json_import_and_convert(jfile)
    print(rgb_from_json)
    # nearest = min(rgb_from_json, key=partial(colorDifference, rgb))
    print("nearest color")
    # print(nearest)
    jfile.close()


def hex_to_rgb(colorstring):
    colorstring = colorstring.strip()
    # if colorstring[0] == '#': colorstring = colorstring[1:]
    if len(colorstring) != 6:
        raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return (r, g, b)

def json_import_and_convert(file):
    jlist = []
    j_dat = json.load(file)
    for i in j_dat['pallete']:
        jlist.append({'name':i['name'],'base':i['base']})
    newj = []
    pprint("jlist: %s" % jlist)
    for hd in jlist:
        if len(hd['base']) == 6:
            newj.append({'name':hd['name'], 'base':hex_to_rgb(hd['base'])})
    pprint("newj: %s" % newj)
    return newj

def colorDifference(testColor, otherColor):
    difference = 0
    difference += abs(testColor[0]-otherColor[0])
    difference += abs(testColor[1]-otherColor[1])
    difference += abs(testColor[2]-otherColor[2])

    return difference
