#!/usr/bin/env python3

"""
* Search Downloads folder for source files
* Ask for file if source not found
* Loop through files
* Generate Xlsx object
* Generate empty Xlsx (output) object
* Check source file for correct info
* Get formatted date range from source file
* Write 'Keep' info to output object
* Format output file cells
* Generate output filename
* Save output file to Downloads folder

I'm breaking this up into a bunch of modules/files just to experiment. 
So, enjoy. ;-)
"""

from re_file_search import get_list
from data import SOURCE_FILENAME, FOLDER, CHECK_VALUE, VALUE_CELL, DATE_CELL
import dropfile
from xlclass import Xlsx
from verify_source import verify_value
from time import sleep
from get_date import get_date


if __name__ == '__main__':
    # Get list of source files from folder
    source_files = get_list(FOLDER, SOURCE_FILENAME)
    
    # Ask for file location if none are found (single list item)
    if not source_files:
        source_files = [dropfile.get()]
        
    for file in source_files:
        # Generate objects
        source_xl = Xlsx(file)
        target_xl = Xlsx()
        
        # Check source for correct contents
        if not verify_value(source_xl, CHECK_VALUE, VALUE_CELL):
            print(f"File contents don't match for:\n{file}\nPlease verify.")
            sleep(2)
            continue
            
        # Get formatted dates
        date_range = get_date(source_xl, DATE_CELL)
        
        pass
        