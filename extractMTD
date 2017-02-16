import xml.etree.ElementTree as ET
import os

'''
@author: hadhafang
'''
class extractMTD:
    """Extract meta data from a metadata folder for the Sentinel project. Will 
    save them in a list.

    Positions:
    0 - id of product
    1 - the start time of the product
    2 - end time of the product
    3 - boleean true if end time equals start time otherwise false
    4 - generation time
    5 - mean cloudiness
    6 - zenith angle
    7 - azimuth angel
    """
    def __init__(self):
        
        self.lst = [None] * 8 # list of the 8 individual meta data
    
    def TimeCloud(self, dir, metadata)
        self.dir = os.chdir(dir)
        self.root = ET.parse(metadata).getroot()
        for Product_Info in self.root.iter('Product_Info'): # Finds product info
            self.lst[0] = Product_Info.find('PRODUCT_URI').text # Product name
            self.lst[1] = Product_Info.find("PRODUCT_START_TIME").text #Start time
            self.lst[2] = Product_Info.find("PRODUCT_STOP_TIME").text #End time or stop time
            self.lst[3] = self.lst[1]==sel.lst[2]                
            self.lst[4] = Product_Info.find("GENERATION_TIME").text   # Gin and Tonic
        
        for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
            self.lst[5] = Quality_Indicators_Info.text
    
    return self.lst
            
    def SunAngle(self, dir, metadata)
    """ Only in granule """
        self.dir = os.chdir(dir)
        self.root = ET.parse(metadata).getroot()
        for Mean_Sun_Angle in self.root.iter('Mean_Sun_Angle'):
            self.lst[6] Mean_Sun_Angle.find('ZENITH_ANGLE').text
            self.lst[7] Mean_Sun_Angle.find('AZIMUTH_ANGLE').text
    
    return self.lst