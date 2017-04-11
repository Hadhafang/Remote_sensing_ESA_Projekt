# Documentation Meta Data
In order to extract, plot and check the data given from Sentinel a number of scripts has to be run. Those are described below:
## IterateMapp.py
IterateMapp.py will create an excel file “Sentinel123.xlsx”. To run this file open the Command-window. Set cd to the filepath where iterateMapp.py is saved. Run “python iterateMapp.py” and a question will appear: “Enter file path to the directories that you want to extract data from e.g  Z:\S2A”.  Answer with the filepath to the parent directory of all sentinel files. 

NOTE! Make sure that your filepath does not contain any swedish letters.

### Sentinel123.xlsx will contain:
Name - The name of the tile set. Used in PlotData.py for making comparisons between tiles with different timestamps
Id - A unique id stamp taken from the metadata file in the topmost  directory
Uri -  A unique id stamp taken from the metadata file in the granule  directory
Clouds - A percentage of clouds extracted form the topmost directory
Start time - A start time from  the metadata file in the topmost  directory
Stop time - A stop time from the metadata file in the topmost directory
Is equal - A comparison between Start time and Stop time. Is true if they’re the same and false otherwise
Generation time - A generation time from the metadata file in the topmost directory
Zenith angle - The zenith angle from the metadata file in the granule  directory
Azimuth angle - The azimuth angle from the metadata file in the granule  directory

The resulting “Sentinel123.xlsx” will be stored in the file path you entered in the Command Window. 
extractMetadata.py
This code extracts metadata out of two given values. First value (dir) states the file path to the metadata-file. Second value (metadata) states the name of the metadata-file where metadata should be extracted. The value of the searched element is then returned.

## PlotData.py
PlotData will parse through the xlsx file and retrieve cloud-data for a specified tile. 
You can enter a cloud level limit to filter out tiles which are too cloudy to use in analysis. 
Input is the directory and filename of the xlsx file.
plotData('C:\Users\Mikael\Downloads','sentinel123.xlsx')

## Checksum.py
A method for checking the md5 checksum in the directory. Will see if the checksum of files and their filename are mentioned in the manifest(manifest.safe). Returns an excel document called “manifestCheck.xlsx” the comparison data will be stored in there. Most checksums for files stored in granule should be represented. The code vill promt the user to:
“Please enter filepath where sought manifest is, e.g Z:\S2a\\33UVB\S2A_MSIL1C_20161208T102422_N0204_R065_T33UVB_20161208T102418.SAFE” 
Enter the path of the directory containing manifest.safe here
Note: Not all files are listed in the manifest. The ones who are interesting ends with .jp2 or .gml and are stored in the subfolders to granule.

## ManifestCheck.xlsx will contain:
File - File name. The ones that should overlapp with the manifest have two True in their rows ends with .jp2 and .gml
File in manifest - Is True if the file is mentioned in “manifest.safe” otherwise false
Md5 - Shows the md5 checksum in hexidigit. If a file wich ends with .jp2 or .gml shows false something has gone wrong with the download.
Md5 in manifest -  Is True if the file is mentioned in “manifest.safe” otherwise False

## Vår Drive mapp
https://drive.google.com/open?id=0BzP2lJTib6lZWEN5SjJCdVVxdlE Projekt mapp med diverse dokument som vi tagit fram under designen.

## Andra kopplade projekt
https://github.com/olivierhagolle/Sentinel-download/blob/master/README.md

https://scihub.copernicus.eu/twiki/do/view/SciHubUserGuide/5APIsAndBatchScripting#Get_product_UUID_from_product_na
