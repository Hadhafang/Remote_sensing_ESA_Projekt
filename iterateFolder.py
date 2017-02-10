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

def extractSunAngle(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()
    result =''
    
    for Mean_Sun_Angle in root.iter('Mean_Sun_Angle'):
        result += '\n' + ('Mean Zenith Angle: ') + Mean_Sun_Angle.find('ZENITH_ANGLE').text
        result += '\n' + ('Mean Azimuth Angle: ') + Mean_Sun_Angle.find('AZIMUTH_ANGLE').text
    
    return result
    
    
os.chdir(r'C:\Mons')

for root, dirs, files in os.walk("C:\Mons"):
    for name in files:
        if name.endswith('.xml'):
            if "MTD" in name:
                print root
                
                print extractSunAngle(root,name)
                