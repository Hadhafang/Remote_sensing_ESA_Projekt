import os, hashlib, mmap

"""
Created on Thu Mar 16 12:04:52 2017

@@ -7,32 +7,45 @@ Created on Thu Mar 16 12:04:52 2017
Will produce MD5 of root folder
"""


def ManifestChecker(p,Sums,Control):
    import xlsxwriter
    assert os.path.exists(p)
    os.chdir(p)
    workbook = xlsxwriter.Workbook('manifestCheck.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'File') # (row, col, data)
    worksheet.write(0, 1, 'File in manifest')
    worksheet.write(0, 2, 'MD5 checksum') # (row, col, data)
    worksheet.write(0, 3, 'MD5 in manifest')

    for index, member in enumerate(Chekkzumz):
        if index % 2 != 1:
            evenIndex = index / 2+1
            worksheet.write(evenIndex, 0,Sums[index])
            worksheet.write(evenIndex, 1,Control[index])
        elif index % 2 != 0:
            oddIndex =index/2+1
            worksheet.write(oddIndex, 2,Sums[index])
            worksheet.write(oddIndex, 3,Control[index])
    workbook.close()
    print 'The excel document "manifestCheck.xlsx" has been made in ' + str(p)

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
    for root, dirs, files in os.walk(directory):
        for fl in files:

            hashVector.append(str(fl))
            hashVector.append(str(hashMaker(root,fl)))
            
            
                    
    return hashVector
    
                
raw_path = raw_input('Please enter filename where sought manifest is, e.g  Z:\S2a\\33UVB\S2A_MSIL1C_20161208T102422_N0204_R065_T33UVB_20161208T102418.SAFE' +'\n')
path = os.path.abspath(raw_path)
assert os.path.exists(path)
Chekkzumz = checksum(path)    
os.chdir(path)
BoolControl = []

with open('manifest.safe','r') as Mfile:
    manifestMEGAstring = mmap.mmap(Mfile.fileno(), 0, access=mmap.ACCESS_READ)
    for cell in Chekkzumz:
        if manifestMEGAstring.find(cell) != -1:
            BoolControl.append(True)
        else:
            BoolControl.append(False)
# Create a workbook and add a worksheet.
ManifestChecker(path,Chekkzumz,BoolControl)
   
