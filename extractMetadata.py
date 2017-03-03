import xml.etree.ElementTree as ET
import os

def extractClouds(dir, metadata):
    os.chdir(dir)
    tree = ET.parse(metadata)
    root = tree.getroot()

    for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
        return Quality_Indicators_Info.text

def extractId(dir, metadata):
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
