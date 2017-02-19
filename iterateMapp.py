import xml.etree.ElementTree as ET
import os

'''
@author: manand83
'''

def walklevel(some_dir, level=10):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

from extractMetadata import extractClouds
os.chdir(r'C:\GISN24')

for root, dirs, files in walklevel('C:\GISN24'):
    for name in files:
        if name.endswith('.xml'):
            if "MTD" in name:
                print root
                print extractClouds(root,name)
