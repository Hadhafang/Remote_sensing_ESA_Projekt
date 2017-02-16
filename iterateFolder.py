
import os
import extractMTD

'''
@author: manand83
'''

        

    
    
class iterateFolder:
    def __init__(self, startDir):
        self.dir = startDir
        self.metadata =[] #a list that will save the meta data components
        os.chdir(self.dir)
        
        for root, dirs, files in os.walk(self.dir):
            for name in files:
                if name.endswith('.xml'):
                    if "MTD" in name:
                        print extractClouds(root,name)
                        print extractSunAngle(root,name)
                
