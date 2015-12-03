import os
import json

from functools import partial
from pprint import pprint

def Palletize(base):
    rgb = hex_to_rgb(base)
    print("Palletizer base rgb: ")
    print(rgb)
    jfile = open(os.getcwd() + '/app/static/pallete.json', 'r')
    jdat = json.load(jfile)
    rgb_from_json = json_import_and_convert(jdat)

    # find closest
    nearest = rgb_from_json[0]
    for item in rgb_from_json:
        if colorDifference(item['base'], rgb) < colorDifference(nearest['base'], rgb):
            nearest = item
    print("nearest color")
    print(nearest)

    # get shades
    pallete = []
    for obj in jdat['pallete']:
        if obj['name'] == nearest['name']:
            pallete.append(obj['base'])
            pallete.append(obj['shades'][0]['1'])
            pallete.append(obj['shades'][1]['2'])
            pallete.append(obj['shades'][4]['5'])
            pallete.append(obj['shades'][9]['10'])

    print("pallete")
    pprint(pallete)
    jfile.close()


def hex_to_rgb(colorstring):
    colorstring = colorstring.strip()
    if len(colorstring) != 6:
        raise ValueError, "input #%s is not in #RRGGBB format" % colorstring
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return (r, g, b)

def json_import_and_convert(j_dat):
    jlist=[]
    for i in j_dat['pallete']:
        jlist.append({'name':i['name'],'base':i['base']})
    newj = []
    for hd in jlist:
        if len(hd['base']) == 6:
            newj.append({'name':hd['name'], 'base':hex_to_rgb(hd['base'])})
    return newj

def colorDifference(testColor, otherColor):
    difference = 0
    difference += abs(testColor[0]-otherColor[0])
    difference += abs(testColor[1]-otherColor[1])
    difference += abs(testColor[2]-otherColor[2])

    return difference
