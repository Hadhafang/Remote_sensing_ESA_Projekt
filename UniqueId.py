# -*- coding: utf-8 -*-
import os
import xlrd
import xml.etree.ElementTree as ET
from urllib2 import urlopen
"""
Created on Fri Mar 17 10:28:52 2017

@author: Mikael
"""

def UniqueId(dir,filename):
    os.chdir(dir)
    wb = xlrd.open_workbook(filename)
    first_sheet = wb.sheet_by_index(0)
    for row in range(first_sheet.nrows):
        URI = first_sheet.cell_value(row+1,1)
        URI = URI[:-5]
        with urlopen("https://scihub.copernicus.eu/dhus/odata/v1/Products?$filter=Name eq " + "'" +URI+"'")as response:
            html = response.read()
            tree = ET.parse(html)
            root = tree.getroot()
            for md5 in root.iter('Checksum'):
                print md5.find('Value').text


UniqueId('C:\Mons','sentinel123.xlsx')        