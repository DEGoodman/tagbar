import os

from pprint import pprint

def make(data):
    f = open(os.getcwd() + '/app/static/css/colors.css', 'w')
    pos_base = ['a', 'b', 'c', 'd', 'e']
    num = 0
    # not sure why data is a nested list
    for quant,col  in data[0]:
        print(quant)
        print(col)
        f.write('#%s' % pos_base[num])
        f.write(' {\n\tbackground-color: rgb') # nastiness
        f.write(str(col))
        f.write(';\n}\n\n')
        num += 1

    pos_comp = ['f', 'g', 'h', 'i', 'j']
    num = 0
    newcols = comp_cols(data)

    f.close()

def comp_cols(data):
    pass
