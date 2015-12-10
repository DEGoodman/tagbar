from __future__ import division

import colorsys
import os
import json
import math

from functools import partial
from pprint import pprint

def Palletize(base):
    rgb = hex_to_rgb(base)
    print("Palletizer base rgb: ")
    print(rgb)
    print("rgb floats:")
    collist = [rgb[0]/255, rgb[1]/255, rgb[2]/255]
    print(collist)
    hsv = colorsys.rgb_to_hsv(collist[0], collist[1], collist[2])
    print("Palletizer base hsv:")
    print(hsv)
    jfile = open(os.getcwd() + '/app/static/pallete.json', 'r')
    jdat = json.load(jfile)
    rgb_from_json = json_import_and_convert(jdat)

    scale = betterDif(hsv)
    nearest = rgb_from_json[0]
    for item in rgb_from_json:
        if item['name'] == scale:
            nearest = item
            print(nearest)

    pallete = []
    for obj in jdat['pallete']:
        if obj['name'] == nearest['name']:
            pallete.append(obj['base'])
            pallete.append(obj['shades'][0]['1'])
            pallete.append(obj['shades'][1]['2'])
            pallete.append(obj['shades'][4]['5'])
            pallete.append(obj['shades'][9]['10'])

    jfile.close()
    pbuild(pallete)
    return pallete


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

def pbuild(lst):
    f = open(os.getcwd() + '/app/static/css/colors.css', 'a')

    pos_base = ['f', 'g', 'h', 'i', 'j']
    num = 0
    # not sure why data is a nested list
    for col in lst:
        f.write('#%s' % pos_base[num])
        f.write(' {\n\tbackground-color: #') # nastiness
        f.write(str(col))
        f.write(';\n}\n\n')
        num += 1

    f.close()

# check hsl values
def betterDif(base):
    # lightness first
    print("h: %s, s: %s, v: %s" % (base[0], base[1], base[2]))
    if base[2] <= 0.12 or base[2] >= 0.97:
        print("greyscale")
        return "Grey"
    # saturation
    elif base[1] <= 0.1:
        print("greyscale")
        return "Grey"
    # color
    else:
        print("color!")
        if base[0] <= 21/365 or base[0] >= 350/360:
            print("Red")
            return "Red"
        elif base[0] >= 331/360:
            print("Pink")
            return "Pink"
        elif base[0] >= 281/360:
            print("Purple")
            return "Purple"
        elif base[0] >= 241/360:
            print("Deep Purple")
            return "Deep Purple"
        elif base[0] >= 221/360:
            print("Indigo")
            return "Indigo"
        elif base[0] >= 201/360:
            print("Blue")
            return "Blue"
        elif base[0] >= 170/360:
            print("Cyan")
            return "Cyan"
        elif base[0] >= 141/360:
            print("Teal")
            return "Teal"
        elif base[0] >= 81/360:
            print("Green")
            return "Green"
        elif base[0] >= 61/360:
            print("Lime")
            return "Lime"
        elif base[0] >= 51/360:
            print("Yellow")
            return "Yellow"
        elif base[0] >= 35/360:
            print("Amber")
            return "Amber"
        else:
            print("Brown")
            return "Brown"
