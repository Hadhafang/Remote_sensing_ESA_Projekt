import xml.etree.ElementTree as ET
import os

'''
@author: manand83
'''
# Retrives the cluod and time stamp content in the MTD file in teh owerarching folder
def extractCloudsTime(dir, metadata):
    os.chdir(dir)
    print os.getcwd()
    print metadata
    tree = ET.parse(metadata)
    root = tree.getroot()
    Quality_Indicators = ''
    
    for Product_Info in root.iter('Product_Info'): # Finds 
        PST = Product_Info.find("PRODUCT_START_TIME").text
        PET = Product_Info.find("PRODUCT_STOP_TIME").text
        GT =  Product_Info.find("GENERATION_TIME").text   # Gin and Tonic
        Quality_Indicators += "\n Product start time" + PST + "\n Product end time" + PET +"\n Generation time" + GT
        if (PET == PST):
             Quality_Indicators += "\n"+ "Product start time equals product end time\ttrue"
        else:
            Quality_Indicators += "\n Product start time equals product end time\tfalse"


    for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
        Quality_Indicators += "\nCloud Coverage Assesment " + str(Quality_Indicators_Info.text)
    return Quality_Indicators
        
# Retriving of the Mtd files        
os.chdir(r'C:\Users\Leonard Berge\Downloads\Mans\T28PDC')
iterations = 0 # Will count the number of iterations to find the meta data files
for root, dirs, files in os.walk("C:\Users\Leonard Berge\Downloads\Mans"):
    for name in files:
        iterations += 1
#        print iterations
        if name.endswith('.xml'):
            if "MTD" in name:
                print "\n" + root
                print "\n" + extractCloudsTime(root,name)
                break
#    print ("\nThere has been:" + str(iterations) + "iterations")
