#!/usr/bin/python

import sys
from os import listdir
from os.path import isfile, join
from subprocess import Popen, PIPE

from brpy import init_brpy
br = init_brpy(br_loc='/usr/local/lib')
br.br_initialize_default()
br.br_set_property('algorithm', 'FaceRecognition')

myfile = open("output.txt", "w")
picpaths = [f for f in listdir('.') if isfile(join('.', f))]
i = 0
for a in picpaths:
    for b in picpaths:
        # p = Popen(['br', '-algorithm','FaceRecognition', '-pairwiseCompare', a, b], stdin=None, stdout=PIPE, stderr=PIPE)
        # output, err = p.communicate()
        # rc = p.returncode
        output = ""
        myfile.write(a+','+b+',')
        br.br_compare(a, b, "output.txt")
        myfile.write('\n')
        i += 1
        if i > 10:
            break
    if i > 10:
        break
myfile.close()


