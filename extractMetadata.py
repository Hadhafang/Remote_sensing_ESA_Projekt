import xml.etree.ElementTree as ET
import os


def extractClouds(dir, metadata):
    os.chdir(dir)
    print os.getcwd()
    print metadata
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
        return Quality_Indicators_Info.text
