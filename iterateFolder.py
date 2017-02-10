import xml.etree.ElementTree as ET
import os

'''
@author: manand83
'''
#class extractInfo:
    
def extractClouds(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()
    result = ''
    for Product_Info in root.iter('Product_Info'): # Finds product info
        PI = Product_Info.find('PRODUCT_URI').text #Product name
        PST = Product_Info.find("PRODUCT_START_TIME").text #Start time
        PET = Product_Info.find("PRODUCT_STOP_TIME").text #End time or stop time
        GT = Product_Info.find("GENERATION_TIME").text   # Gin and Tonic
        result += "\n Product Name: " +PI +  "\n Product start time: " + PST + "\n Product end time: " + PET +"\n Generation time: " + GT
       

    for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
        result+= Quality_Indicators_Info.text
    
    return result
    
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
                print extractClouds(root,name)
                print extractSunAngle(root,name)
                