import xml.etree.ElementTree as ET
import os

# os.chdir(r'C:\GISN24\Projekt')
os.chdir(r'C:\GISN24') # Vi borde nog kopiera deras system
print os.getcwd()

# for root, dirs, files in os.walk("Z:\S2a\28PDC"):
#     for name in files:
#         if name.endswith('.xml'):
#             print os.sep.join([dirpath, filename])
iterations = 0
for root, dirs, files in os.walk("C:\GISN24"):
    iterations  += 1
    for name in files:
        if name.endswith('.xml'):
            print(os.path.join(root, name))
        # a.append(os.path.join(root,name))
    for name in dirs:
        if name.endswith('.xml'):
            print(os.path.join(root, name))
        # b.append(os.path.join(root,name))
    print("there has been " + iterations +"iterations")
# tree = ET.parse('MTD_MSIL1C.xml')
# root = tree.getroot()
#
#
# for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
#     print Quality_Indicators_Info.text
