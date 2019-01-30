# FlightRadar2OpenFlights converter
-----------------
There is no way to import your flights history from my.flightradar24.com to openflights.org. But both sites have import/export functions for backup. 
There are different formats in csv files, so you should use my converter. 

# Usage:
-----------------
1. Export your flights history from <https://my.flightradar24.com/settings/export>
2. Use my phyton script in command line: 
```
flightradar2openflights.py -s SOURCE_FILE_NAME -d DEST_FILE_NAME
```
3. Import flights history on <https://openflights.org/html/import>

# Files:
Name  | Description
----------------|----------------------
flightradar2openflights.py       | Phyton script for converting exported files
flightdiary_example.csv          | Exported file from <https://my.flightradar24.com/igorbasic>
openflights_example.csv          | Result file for import (example on <https://openflights.org/user/igorbasic>)
