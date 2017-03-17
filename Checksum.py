# -*- coding: utf-8 -*-
import os, hashlib
"""
Created on Thu Mar 16 12:04:52 2017

@author: Hadhafang
"""


class checksum:
    def __init__(self, dir):
        self.dir = dir
        
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