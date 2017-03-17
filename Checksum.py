# -*- coding: utf-8 -*-
import os, hashlib
"""
Created on Thu Mar 16 12:04:52 2017

@author: Hadhafang
Will produce MD5 of root folder
"""


def checksum (dir):
    dir = os.path.abspath(dir)
    md5 = hashlib.md5()
    for root,dirs files in os.walk(dir):
        for name in files:
            filepath = os.path.join(root,names) # joins the path and the file.
        try:
          f1 = open(filepath, 'rb')
        except:
          # You can't open the file for some reason
          f1.close()
          continue
    while 1:
        buf = f1
    
        
#   SHAhash = hashlib.md5()
#   for root, dirs, files in os.walk(dir):
#      for names in files:
#          filepath = os.path.join(root,names)
#   while 1:
#      # Read file in as little chunks
#      buf = f1.read(4096)
#      if not buf : break
#      SHAhash.update(hashlib.md5(buf).hexdigest())
#
#      
#checksum(os.path.abspath('C:\Logg\33UVB\S2A_MSIL1C_20161208T102422_N0204_R065_T33UVB_20161208T102418.SAFE')