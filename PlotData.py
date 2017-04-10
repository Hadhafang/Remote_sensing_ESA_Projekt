import os
import xlrd
import matplotlib.pyplot as plt


#tilename tabellnamn.  x-axel -> start/stop time.  y-axel cloud
'''
@author: Mikael
Uses the excel-document to plot the different cloudiness values of a tile. X-axis is based on start time, and y-axis dictates how cloudy the tile is.
'''

def plot(dir,filename):
   os.chdir(dir)
   wb = xlrd.open_workbook(filename)
   first_sheet = wb.sheet_by_index(0)
   xticks = []
   x = []
   y = []
   counter = 0
   name = raw_input('Please enter sought tilename, e.g. 28PDC' +'\n')
   limit = raw_input('Would you like to set a cloud factor limit? y/n' +'\n')
   if(limit == 'y'):
       lim = input('Set a cloud limit, for example 50. 0 is total lack of clouds and 100 is full cloudiness.' + '\n' )
       for row in range(first_sheet.nrows):
           if name == first_sheet.cell_value(row,0):
               if(int(float(first_sheet.cell_value(row,2)))<lim):
                   x.append(row)
                   xticks.append([first_sheet.cell_value(row,3)])
                   y.append(first_sheet.cell_value(row,2))
               counter+=1
   else:
       for row in range(first_sheet.nrows):
           if name == first_sheet.cell_value(row,0):
               x.append(row)
               xticks.append([first_sheet.cell_value(row,3)])
               y.append(first_sheet.cell_value(row,2))
           counter+=1
   plt.title(name)   
   plt.tick_params(axis='both', which='major', labelsize=13)
   plt.tick_params(axis='both', which='minor', labelsize=10)
   plt.ylim(0,100,10)      
   plt.xlabel('Start time',fontsize =14)
   plt.ylabel('Cloudiness',fontsize =14)
   plt.xticks(x,xticks,rotation=15)
   plt.bar(x,y)        
   plt.show()
   
   if counter == 0:   
       print('There is no such tilename')
       



plot('C:\Users\Mikael\Downloads','sentinel123.xlsx')

       