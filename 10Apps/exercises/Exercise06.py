#!/usr/bin/env python3
import os
import glob
import zipfile
from datetime import datetime
compressed_file = zipfile.ZipFile("Sample-Files.zip", 'r')
compressed_file.extractall('.')
compressed_file.close()
now = datetime.timetuple(datetime.now())
outfilename = '-'.join(map(str,now))

files = glob.glob('file?.txt')
outfile = open(outfilename + '.txt', 'a+')
for txtfilename in files:
    with open(txtfilename, 'r') as txtfile:
        outfile.write(txtfile.read())

