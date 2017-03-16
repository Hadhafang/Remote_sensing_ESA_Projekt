import xml.etree.ElementTree as ET
import os
import xlsxwriter

'''
@author: manand83
'''

# -------------------------------------------------------------
# METHOD THAT DEFINES HOW DEEP THE ITERATION WILL GO, IF LEVEL
# IS SET TO 2 THE ITERATION WILL GO 2 FOLDERS DEEP AND NOT FURHTER
# -------------------------------------------------------------
def walklevel(some_dir, level):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]
# -------------------------------------------------------------
# DECLARE VECTORS TO STORE METADATA
# -------------------------------------------------------------
names = [] # name of the product (ex 28PDC)
id = [] # id of the product
cloud = [] # percentage cloud coverage
startTime = [] #the start time of the product
stopTime = [] # the stop time of the product
timeEqual = [] # boleean true if end time equals start time otherwise false
genTime = [] # generation time
zenithAngle = [] # zenith angle
azimuthAngle = [] # azimuth angle
# -------------------------------------------------------------
# IMPORT METHODS TO EXTRACT METADATA FROM XML-DOCUMENT
# -------------------------------------------------------------
from extractMetadata import extractClouds
from extractMetadata import extractId
from extractMetadata import extractStartTime
from extractMetadata import extractStopTime
from extractMetadata import extractGenTime
from extractMetadata import extractZenithAngle
from extractMetadata import extractAzimuthAngle

# -------------------------------------------------------------
# STORES THE NAME OF THE TOP FOLDER (ex S2A)
# -------------------------------------------------------------

os.chdir(BootRoot)
directories = []
productname = []
for root, dirs, files in walklevel(BootRoot, 0):
    for i, item in enumerate(dirs):
        directories.append(os.path.join(root, dirs[i])) # ex ['C:\\GISN24\\28PDC', 'C:\\GISN24\\32VPR']
        productname.append(dirs[i]) # ex ['28PDC', '32VPR']
folders = 0
for i, item in enumerate(directories):
    for root, dirs, files in walklevel(directories[i],0):
        folders += len(dirs) # count number of folders in every ['C:\\GISN24\\28PDC', 'C:\\GISN24\\32VPR']
        for n in range(folders):
            names.append(productname[i])
        folders = 0 # set to 0 to count next next folder

# -------------------------------------------------------------
# ITERATION EXTRACTING INFORMATION FROM THE FIRST METADATA-FILE
# -------------------------------------------------------------
os.chdir(BootRoot)
for root, dirs, files in walklevel(BootRoot, 2):
    for name in files:
        if name.endswith('.xml'):
            if "MTD" in name:
                cloud.append(extractClouds(root,name))
                id.append(extractId(root,name))
                startTime.append(extractStartTime(root,name))
                stopTime.append(extractStopTime(root,name))
                genTime.append(extractGenTime(root,name))

# -------------------------------------------------------------
# ITERATION EXTRACTING  INFORATION FROM THE GRANULE FOLDER
# -------------------------------------------------------------
for root, dirs, files in walklevel(BootRoot, 3):
    for name in dirs:
        if root.endswith('GRANULE'): # finds folder "GRANULE" and saves the path to "directory"
            directory = root
            for root, dirs, files in walklevel(directory, 3):
                for name in files:
                    if name.endswith('.xml'):
                        if "MTD" in name:
                            zenithAngle.append(extractZenithAngle(root,name))
                            azimuthAngle.append(extractAzimuthAngle(root,name))

# -------------------------------------------------------------
# CHECK IF START TIME AND STOP TIME IS EQUAL
# -------------------------------------------------------------
for i,item in enumerate(startTime):
     timeEqual.append(startTime[i] == stopTime[i]) #returns true if the time is equal


# -------------------------------------------------------------
# EXPORT METADATA TO EXCEL SHEET
# -------------------------------------------------------------
os.chdir(BootRoot) #Specifies where to save the file
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('sentinel123.xlsx')
worksheet = workbook.add_worksheet()

# Sets heading to columns
worksheet.write(0, 0, 'Name') # (row, col, data)
worksheet.write(0, 1, 'Id') # (row, col, data)
worksheet.write(0, 2, 'Clouds')
worksheet.write(0, 3, 'Start time')
worksheet.write(0, 4, 'Stop time')
worksheet.write(0, 5, 'Is equal')
worksheet.write(0, 6, 'Generation time')
worksheet.write(0, 7, 'Zenith angle')
worksheet.write(0, 8, 'Asimuth angle')

# Walks through every list and puts the information in correct cell
for index, member in enumerate(id):
     worksheet.write(index+1, 0,names[index])
     worksheet.write(index+1, 1,id[index])
     worksheet.write(index+1, 2,cloud[index])
     worksheet.write(index+1, 3,startTime[index])
     worksheet.write(index+1, 4,stopTime[index])
     worksheet.write(index+1, 5,timeEqual[index])
     worksheet.write(index+1, 6,genTime[index])
     worksheet.write(index+1, 7,zenithAngle[index])
     worksheet.write(index+1, 8,azimuthAngle[index])

workbook.close()
