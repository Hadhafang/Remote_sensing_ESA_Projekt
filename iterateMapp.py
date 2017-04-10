import sys
import os
import xlsxwriter
'''
@author: manand83
'''
# -------------------------------------------------------------
# DECLARE VECTORS TO STORE METADATA
# -------------------------------------------------------------
names = [] # name of the product (ex 28PDC)
id = [] # tile-id of the product
uri = [] # uri of the product
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
from extractMetadata import extractURI
from extractMetadata import extractID
from extractMetadata import extractStartTime
from extractMetadata import extractStopTime
from extractMetadata import extractGenTime
from extractMetadata import extractZenithAngle
from extractMetadata import extractAzimuthAngle
from WalkLevel       import walklevel
# -------------------------------------------------------------
# STORES THE NAME OF THE TOP FOLDER (ex S2A)
# -------------------------------------------------------------
BootRoot = os.path.abspath('C:\GISN24') #Store the deafult path here

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
# ITERATION EXTRACTING INFORMATION FROM THE METADATA-FILE IN TOP-MOST FOLDER
# -------------------------------------------------------------
os.chdir(BootRoot)
for root, dirs, files in walklevel(BootRoot, 2):
    for name in files:
        if name.endswith('.xml'):
            if "MTD" in name:
                cloud.append(extractClouds(root,name))
                uri.append(extractURI(root,name))
                startTime.append(extractStartTime(root,name))
                stopTime.append(extractStopTime(root,name))
                genTime.append(extractGenTime(root,name))

# -------------------------------------------------------------
# ITERATION EXTRACTING INFORMATION FROM THE GRANULE FOLDER
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
                            id.append(extractID(root,name))

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

worksheet.write(0, 1, 'ID')
worksheet.write(0, 2, 'URI') # (row, col, data)
worksheet.write(0, 3, 'Clouds')
worksheet.write(0, 4, 'Start time')
worksheet.write(0, 5, 'Stop time')
worksheet.write(0, 6, 'Is equal')
worksheet.write(0, 7, 'Generation time')
worksheet.write(0, 8, 'Zenith angle')
worksheet.write(0, 9, 'Asimuth angle')



# Walks through every list and puts the information in correct cell
for index, member in enumerate(id):
     worksheet.write(index+1, 0,names[index])
     worksheet.write(index+1, 1,id[index])
     worksheet.write(index+1, 2,uri[index])
     worksheet.write(index+1, 3,cloud[index])
     worksheet.write(index+1, 4,startTime[index])
     worksheet.write(index+1, 5,stopTime[index])
     worksheet.write(index+1, 6,timeEqual[index])
     worksheet.write(index+1, 7,genTime[index])
     worksheet.write(index+1, 8,zenithAngle[index])
     worksheet.write(index+1, 9,azimuthAngle[index])

workbook.close()
