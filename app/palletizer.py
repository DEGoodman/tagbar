import os
import json


from pprint import pprint

def Palletize(base):
    rgb = hex_to_rgb(base)
    print("Palletizer base rgb: ")
    print(rgb)
    jfile = open(os.getcwd() + '/app/static/pallete.json', 'r')
    rgb_from_json = json_import_and_convert(jfile)
    vals = find_closest(rgb, rgb_from_json)
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
        jlist.append(i['base'])
    # pprint(jlist)
    newj = []
    for hd in jlist:
        if len(hd) == 6:
            newj.append(hex_to_rgb(hd))
    pprint("newj: %s" % newj)
    return newj

def find_closest(target, lst):
    print("looking for closest to %s in %s" % (target, lst))
