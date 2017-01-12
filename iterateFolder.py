import xml.etree.ElementTree as ET
import os

'''
@author: manand83
'''

def extractClouds(dir, metadata):
    os.chdir(dir)
    print os.getcwd()
    print metadata
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
        return Quality_Indicators_Info.text

os.chdir(r'C:\GISN24')

for root, dirs, files in os.walk("C:\GISN24"):
    for name in files:
        if name.endswith('.xml'):
            if "MTD" in name:
                print root
                print extractClouds(root,name)
