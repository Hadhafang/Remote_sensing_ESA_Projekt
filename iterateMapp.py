import xml.etree.ElementTree as ET
import os

# os.chdir(r'C:\GISN24\Projekt')
os.chdir(r'C:\GISN24')
print os.getcwd()

# for root, dirs, files in os.walk("Z:\S2a\28PDC"):
#     for name in files:
#         if name.endswith('.xml'):
#             print os.sep.join([dirpath, filename])

for root, dirs, files in os.walk("C:\GISN24"):
    for name in files:
        if name.endswith('.xml'):
            print(os.path.join(root, name))
        # a.append(os.path.join(root,name))
    for name in dirs:
        if name.endswith('.xml'):
            print(os.path.join(root, name))
        # b.append(os.path.join(root,name))

# tree = ET.parse('MTD_MSIL1C.xml')
# root = tree.getroot()
#
#
# for Quality_Indicators_Info in root.iter('Cloud_Coverage_Assessment'):
#     print Quality_Indicators_Info.text
