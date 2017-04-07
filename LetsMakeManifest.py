# -*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET
import glob

"""
Created on Mon Apr 03 18:59:45 2017

@author: Leonard Berge
"""
def existanceAsserter(object):
    assert object is not None
    return str(object)+'does exist'
    
def iterateManifest(path):
    print 'goten'
   # nameSpace = {'xfdu':"urn:ccsds:schema:xfdu:1", \
   #              'safe':"http://www.esa.int/safe/sentinel/1.1",\
   #              'gml':"http://www.opengis.net/gml",\
   #              'xmlns' :"http://www.esa.int/safe/sentinel/1.1"}
    assert os.path.exists(path)
    os.chdir(path)
    #theManifest = glob.glob('*manifest.safe')
    assert os.path.isfile('manifest.safe')
    tree = ET.parse('manifest.safe')
    print existanceAsserter(tree)
    root = tree.getroot()
    print existanceAsserter(root)
    vector = [None]
    print existanceAsserter(root.findtext('byteStream'))
    for subroot in root.findall('checksum'):
        print 'in for'
        print subroot.tag
        row = [subroot.find('fileLocation')]
        row.append[]
        print str(directory)
    return vector
    
raw_path = raw_input('Please enter filename where sought manifest is, e.g  Z:\S2a\\33UVB\S2A_MSIL1C_20161208T102422_N0204_R065_T33UVB_20161208T102418.SAFE' +'\n')
directory = os.path.abspath(raw_path)
assert os.path.exists(directory)
os.chdir(directory)
Answer = iterateManifest(directory)

