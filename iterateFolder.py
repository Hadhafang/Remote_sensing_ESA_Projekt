
import os
import extractMTD

'''
@author: manand83, hadhafang
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
                        self.metadata.append.extractMTD #it should only append witth the outhermost mtd
                        self.metadata[-1].TimeCloud(root,name) #For the outermost mtd
                        self.metadata[-1].SunAngle(root,name) #This will always be wrong now
                        # print extractClouds(root,name)
                        # print extractSunAngle(root,name)
        return self.metadata
        
                
