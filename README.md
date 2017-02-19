# Fj-rAnalys
Kod för att analysera filer från ESA sentinel
Ska svara på hur stor del av en tile som är molnig
Om en tile är hel

## renderTileList
Skapar en funktion på det här formatet med alla fungerande tiles i ett givet directory:
2017-2-17 9
id      start_time      stop_time       start_equals_end        generation_time Cloud_Coverage_Assessment       Zenith_angel    Azimuth_angel
S2A_MSIL1C_20161206T112442_N0204_R037_T28PDC_20161206T112747.SAFE	2016-12-06T11:24:42.026Z	2016-12-06T11:24:42.026Z	true	0.0	42.6044113484919	153.706102168869

##tileFinder
hittar efter en tile och presenterar data kring den.
33WRX, 34VDR verkar trasig

iterateMapp.py är ett första försök till att iterera genom en mapp för att hitta rätt fil. I vår fall filer innehållandes metadata

iterateFolder.py extraherar information om molnighet i angiven mapPythop. Funktionen hittar alla filer som avslutas med ".xml" samt innehåller texten "MTD". För varje mapp hittas tre sådana filer (endast en behövs). För varje fil hittas elementet "Cloud_Coverage_Assessment" och dess värde returneras.
## Vår Drive mapp
https://drive.google.com/open?id=0BzP2lJTib6lZWEN5SjJCdVVxdlE Projekt mapp med diverse dokument som vi tagit fram under designen.

## Andra kopplade projekt
https://github.com/olivierhagolle/Sentinel-download/blob/master/README.md
