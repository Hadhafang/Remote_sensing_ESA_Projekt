import xml.etree.ElementTree as ET
import os

'''
@author: manand83
'''
# Retrives the clod content in the MTD file in teh owerarching folder
def extractClouds(dir, metadata):
    os.chdir(dir)
    print os.getcwd()
    print metadata
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
        return Quality_Indicators_Info.text

# Retriving of the Mtd files        
os.chdir(r'C:\Users\Leonard Berge\Downloads\Mans')
iterations = 0 # Will count the number of iterations to find the meta data files
for root, dirs, files in os.walk("C:\Users\Leonard Berge\Downloads\Mans"):
    for name in files:
        iterations += 1
        if name.endswith('.xml'):
            if "MTD" in name:
                print "\n" + root
                print "\n" + extractClouds(root,name)
        print ("\n There has been:" + str(iterations) + "iterations")
