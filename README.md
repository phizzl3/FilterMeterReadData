# FilterMeterReadData

 Gets raw meter reads dump from TRAC and outputs just the needed info.

* Has all user variables housed in and imported from user_values.py
* Searches Downloads folder for source files
* Asks for file if source not found
* Loops through files
* Generates Xlsx object from source
* Generates empty Xlsx (output) object
* Checks source file for correct info
* Gets formatted date range from source file
* Writes 'Keep' info to output object
* Formats output file cells
* Generates output filename
* Saves output file to Downloads folder

I'm breaking this up into a bunch of modules/files just to experiment.  
So, enjoy. ;-)

## Requirements

python == 3.6+  
openpyxl==3.0.6


## Usage

Run as script

```bash
$ python3 filter_meter_data
```
