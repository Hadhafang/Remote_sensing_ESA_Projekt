# -*- coding: utf-8 -*-
import os
"""
Created on Thu Mar 16 12:04:52 2017

@author: Hadhafang
Will produce MD5 of root folder
"""

from iterateMapp import walklevel


        

def checksum (dir):
# -------------------------------------------------------------
# A HELP FUNKTION THAT MAKES THE ACTUALL HASH
# -------------------------------------------------------------
    
    def hashMaker(dir, file):
        import hashlib
        os.chdir(dir)
        hasher = hashlib.md5()
        with open(file, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
            return hasher.hexdigest()
# -------------------------------------------------------------
# ACTUALL CHECKSUM CODE
# -------------------------------------------------------------    
    directory = os.path.abspath(dir)
    
    hashMatrix= [['Inspire',0],['Manifest',0],['Mtd',0]]
    for root, dirs, files in walklevel(directory, 0):
        for name in files:
    #These three should be the only files in files but the checking is for safty
            if name.endswith('INSPIRE.xml'):
                hashMatrix [0][1] = hashMaker(root,name)  
            elif name.endswith('manifest.safe'):
                hashMatrix [1][1]  = hashMaker(root,name)
            elif name.endswith('.xml'):
                if "MTD" in name:
                   hashMatrix [2][1]  = hashMaker(root, name)
            
            
                    
    return hashMatrix
    
                
path = os.path.abspath(r'c:\logg\33uvb\s2a_msil1c_20161208t102422_n0204_r065_t33uvb_20161208t102418.safe')
print checksum(path)    