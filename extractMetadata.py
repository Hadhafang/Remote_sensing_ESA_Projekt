import xml.etree.ElementTree as ET
import os
import re
import fnmatch

#Extracts cloudness from element Cloud_Coverage_Assessment from MTD in top-most folder
def extractClouds(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
        return Quality_Indicators_Info.text

#Extracts tile-id from element TILE_ID from MTD in GRANULE folder
def extractID(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for TILE_ID in root.iter('TILE_ID'):
        return TILE_ID.text

    for TILE_ID_2A in root.iter('TILE_ID_2A'):
        return TILE_ID_2A.text

#Extracts URI from element PRODUCT_URI from MTD in top-most folder
def extractURI(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Product_Info in root.iter('Product_Info'):
        return Product_Info.find('PRODUCT_URI').text

    for L2A_Product_Info in root.iter('L2A_Product_Info'):
        return L2A_Product_Info.find("PRODUCT_URI").text

#Extracts start time from element PRODUCT_START_TIME from MTD in top-most folder
def extractStartTime(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Product_Info in root.iter('Product_Info'):
        return Product_Info.find("PRODUCT_START_TIME").text

    for L2A_Product_Info in root.iter('L2A_Product_Info'):
        return L2A_Product_Info.find("PRODUCT_START_TIME").text

#Extracts stop time from element PRODUCT_STOP_TIME from MTD in top-most folder
def extractStopTime(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Product_Info in root.iter('Product_Info'):
        return Product_Info.find("PRODUCT_STOP_TIME").text

    for L2A_Product_Info in root.iter('L2A_Product_Info'):
        return L2A_Product_Info.find("PRODUCT_STOP_TIME").text

#Extracts generation time from element GENERATION_TIME from MTD in top-most folder
def extractGenTime(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Product_Info in root.iter('Product_Info'):
        return Product_Info.find("GENERATION_TIME").text

    for L2A_Product_Info in root.iter('L2A_Product_Info'):
        return L2A_Product_Info.find("GENERATION_TIME").text

#Extracts zenith angle from element ZENITH_ANGLE from MTD in GRANULE folder
def extractZenithAngle(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Mean_Sun_Angle in root.iter('Mean_Sun_Angle'):
        return Mean_Sun_Angle.find("ZENITH_ANGLE").text

#Extracts azimuth angle from element AZIMUTH_ANGLE from MTD in GRANULE folder
def extractAzimuthAngle(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Mean_Sun_Angle in root.iter('Mean_Sun_Angle'):
        return Mean_Sun_Angle.find("AZIMUTH_ANGLE").text
