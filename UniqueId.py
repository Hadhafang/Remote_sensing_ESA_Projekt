# -*- coding: utf-8 -*-
import os
import xlrd
from lxml import etree
from urllib2 import urlopen
import requests
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
        url = 'https://scihub.copernicus.eu/dhus/odata/v1/Products?$filter=Name eq '+"'" +URI +"'"
        auth = ('username','password')
        r = requests.get(url,auth=auth)
        result = r.content
        tree = etree.parse(result)
        root = tree.getroot()
        for md5 in root.iter('d:properties'):
            print md5.find('d:Value').text
        

UniqueId('C:\Mons','sentinel123.xlsx')        