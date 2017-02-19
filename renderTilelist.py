import datetime
import os
#import iterateFolder

'''
@author: hadhafang
render a list of all tiles and certain parts of their meta data.
'''
dir = os.chdir(r'C:\Mons') #change it to the path as needed
files = iterateFolder(dir)


open('SentinelList.txt','w') # Name of file. 'w' indicates write
now = datetime.datetime.now()
# string buliding or rather table building
year = now.year
month = now.month
day = now.day
hour = now.hour


rT = year + '-'+ month + '-' + day + ' ' + hour +'\n' #Rendering time a time stamp


table = rT + 'id\tstart_time\tstop_time\tstart_equals_end\tgeneration_time\tCloud_Coverage_Assessment\tZenith_angel\tAzimuth_angel'
for file in files: # iterates through the file list
    table += '\n'
    for data in file: # iterates through the list of metadata
        table += str(data) +'\t'
        