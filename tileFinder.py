import xml.etree.ElementTree as ET
import os
import xlrd
import numpy as np
import matplotlib.pyplot as plt


#tilename tabellnamn.  x-axel -> start/stop time.  y-axel cloud
'''
@author: Mikael
Plots 
'''

def test(dir,filename):
   os.chdir(dir)
   wb = xlrd.open_workbook(filename)
   first_sheet = wb.sheet_by_index(0)
   xticks = []
   for row in range(first_sheet.nrows):
        xticks.append(first_sheet.cell_value(row+1,3))
   for row in range(first_sheet.nrows):
       x = [row]
      
       cld = first_sheet.cell_value(row+1,2)
       plt.title(first_sheet.cell_value(row+1,0))
       plt.xticks(x,xticks,rotation=90)
       plt.plot(cld,x,'*')
       
       plt.show()
      
       
       
test('C:\Users\Mikael\Downloads','sentinel123.xlsx')
       