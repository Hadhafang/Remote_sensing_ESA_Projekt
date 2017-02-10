import xml.etree.ElementTree as ET
import os

'''
@author: manand83
'''
<<<<<<< HEAD
# Retrives the cloud and time stamp content in the MTD file in teh owerarching folder
def extractCloudsTime(dir, metadata):
=======
#class extractInfo:
    
def extractClouds(dir, metadata):
>>>>>>> refs/remotes/origin/MikaelBranch2
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()
<<<<<<< HEAD
    Quality_Indicators =''
    
    for Product_Info in root.iter('Product_Info'): # Finds product info
        PST = Product_Info.find("PRODUCT_START_TIME").text #Start time
        #Quality_Indicators += "\n Product start time" + PET
        PET = Product_Info.find("PRODUCT_STOP_TIME").text #End time or stop time
        GT = Product_Info.find("GENERATION_TIME").text   # Gin and Tonic
        Quality_Indicators += "\n Product start time" + PST + "\n Product end time" + PET +"\n Generation time" + GT
        print Quality_Indicators

    for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
        Quality_Indicators += "\n Cloud Coverage Assesment " + str(Quality_Indicators_Info.text)
    return Quality_Indicators
        
# Retriving of the Mtd files        
os.chdir(r'C:\Users\Leonard Berge\Downloads\Mans\T28PDC')
iterations = 0 # Will count the number of iterations to find the meta data files
for root, dirs, files in os.walk("C:\Users\Leonard Berge\Downloads\Mans\T28PDC"):
=======
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
>>>>>>> refs/remotes/origin/MikaelBranch2
    for name in files:
        iterations += 1
        if name.endswith('.xml'):
            if "MTD" in name:
<<<<<<< HEAD
                print "\n" + root
                print "\n" + extractCloudsTime(root,name)
                break
    print ("\n There has been:" + str(iterations) + "iterations")
=======
                print extractClouds(root,name)
                print extractSunAngle(root,name)
                
>>>>>>> refs/remotes/origin/MikaelBranch2
