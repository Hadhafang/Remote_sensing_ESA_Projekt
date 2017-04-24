import os
import xlrd
import matplotlib.pyplot as plt


#tilename tabellnamn.  x-axel -> start/stop time.  y-axel cloud
'''
@author: Mikael
Uses the excel-document to plot the different cloudiness values of a tile. X-axis is based on start time, and y-axis dictates how cloudy the tile is.
'''

def plotData(dir,filename):
   os.chdir(dir)
   wb = xlrd.open_workbook(filename)
   first_sheet = wb.sheet_by_index(0)
   yticks = []
   x = []
   y = []
   counter = 0 # ugly way to test if tile-name actually exists. it works though
   
   
   name = raw_input('Please enter sought tilename, e.g. 28PDC' +'\n')
   limit = raw_input('Would you like to set a cloud factor limit? y/n' +'\n')
   
   
   if(limit == 'y'):
       lim = input('Set a cloud limit, for example 50.' + '\n' + '0 is total lack of clouds and 100 is full cloudiness.' + '\n' )
       for row in range(first_sheet.nrows):
           if name == first_sheet.cell_value(row,0): 
               if(int(float(first_sheet.cell_value(row,2)))<lim):
                   y.append(row)
                   start_time = first_sheet.cell_value(row,3)
                   start_time = start_time[:-11]
                   yticks.append(start_time)
                   x.append(first_sheet.cell_value(row,2))
                   counter+=1
   else:
       for row in range(first_sheet.nrows):
           if name == first_sheet.cell_value(row,0):
               y.append(row)
               start_time = first_sheet.cell_value(row,3)
               start_time = start_time[:-11]
               yticks.append(start_time)
               x.append(first_sheet.cell_value(row,2))
               counter+=1
           
# -------------------------------------------------------------
# Plots the cloud data with the help of matplotlib. Plots the data as a bar plot
# -------------------------------------------------------------        
   
   if counter == 0:   
       print('There is no such tilename')
   else:
       plt.title(name)   
       plt.tick_params(axis='both', which='major', labelsize=13)
       plt.tick_params(axis='both', which='minor', labelsize=10)
       plt.xlim(0,100,10)       
       plt.ylabel('Start time',fontsize =14)
       plt.xlabel('Cloudiness',fontsize =14)    
       plt.yticks(y,yticks)
       plt.barh(y,x,align ='center')        
       plt.show()
   
       



#plotData('C:\Logg','sentinel123.xlsx')

       