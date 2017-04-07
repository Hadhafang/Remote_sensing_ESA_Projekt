import xml.etree.ElementTree as ET
import os
import re
import fnmatch

def extractClouds(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
        return Quality_Indicators_Info.text

def extractID(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for TILE_ID in root.iter('TILE_ID'):
        return TILE_ID.text

    for TILE_ID_2A in root.iter('TILE_ID_2A'):
        return TILE_ID_2A.text

def extractURI(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Product_Info in root.iter('Product_Info'):
        return Product_Info.find('PRODUCT_URI').text

    for L2A_Product_Info in root.iter('L2A_Product_Info'):
        return L2A_Product_Info.find("PRODUCT_URI").text

def extractStartTime(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Product_Info in root.iter('Product_Info'):
        return Product_Info.find("PRODUCT_START_TIME").text

    for L2A_Product_Info in root.iter('L2A_Product_Info'):
        return L2A_Product_Info.find("PRODUCT_START_TIME").text

def extractStopTime(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Product_Info in root.iter('Product_Info'):
        return Product_Info.find("PRODUCT_STOP_TIME").text

    for L2A_Product_Info in root.iter('L2A_Product_Info'):
        return L2A_Product_Info.find("PRODUCT_STOP_TIME").text

def extractGenTime(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Product_Info in root.iter('Product_Info'):
        return Product_Info.find("GENERATION_TIME").text

    for L2A_Product_Info in root.iter('L2A_Product_Info'):
        return L2A_Product_Info.find("GENERATION_TIME").text

def extractZenithAngle(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Mean_Sun_Angle in root.iter('Mean_Sun_Angle'):
        return Mean_Sun_Angle.find("ZENITH_ANGLE").text

def extractAzimuthAngle(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Mean_Sun_Angle in root.iter('Mean_Sun_Angle'):
        return Mean_Sun_Angle.find("AZIMUTH_ANGLE").text
def TileId(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()
    for GI in root.iter('TILE_ID')
        return GI.text
