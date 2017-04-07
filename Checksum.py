import os, hashlib

"""
Created on Thu Mar 16 12:04:52 2017

@@ -7,32 +7,45 @@ Created on Thu Mar 16 12:04:52 2017
Will produce MD5 of root folder
"""

from WalkLevel import walklevel


        

def checksum (dir):
    directory = os.path.abspath(dir)
# -------------------------------------------------------------
# A HELP FUNKTION THAT MAKES THE ACTUALL HASH
# -------------------------------------------------------------
    
    def hashMaker(dir, file):
        os.chdir(dir)
        hasher = hashlib.md5()
        with open(file, 'rb') as afile:
            buf = afile.read()
            hasher.update(buf)
            return hasher.hexdigest()
# -------------------------------------------------------------
# ACTUALL CHECKSUM CODE
# -------------------------------------------------------------    
    
    
    hashVector= []
    for root, dirs, files in walklevel(directory, 2):
        for fl in files:
    #These three should be the only files in files but the checking is for safty
            hashVector.append(hashMaker(root,fl))
            
            
                    
    return hashVector
    
                
path = os.path.abspath(r'C:\Logg\28PDC\S2A_OPER_PRD_MSIL1C_PDMC_20160122T001801_R037_V20160121T113930_20160121T113930.SAFE\GRANULE')
print checksum(path)    
