# hpe-warranty-lookup

Python script for looking up active warranties on HPE servers.

## Requirements
* BeautifulSoup
* Python3

## Usage
./hpe-warranty-lookup.py <Serial_Number>

## To-Do
* Merge multiple lookup with single lookup
* * Potentially have the script check to see if a file exists with the name specified as an argument.  Fail back to single serial if it doesnt exist.
* * Or, more simple, use "-f <filename>" to designate file
