"""
This is all of the user variables and values. I stuck them all together
so they're easy to find and update without having to look through the 
scripts. They can be easily accessed by importing this module. 
"""

from pathlib import Path

# Source file search expression (regex)
SOURCE_FILENAME = r'Meter_Reads_Data_Dump.*\.xlsx'

# Folder to search for source files (User's Downloads folder)
# This will also be the output folder for the target files
FOLDER = Path().home().resolve() / "Downloads"

# Columns from source files containing the needed info
KEEP_COLUMNS = ('A', 'B', 'C', 'D', 'E', 'F', 'H',
                'J', 'K', 'N', 'P', 'BF', 'BK', 'CC')

# Value to verify to check that we're using the correct source file
CHECK_VALUE = 'Meter Read Data Dump'

# Cell to check when verifying info for CHECK_VALUE matches
VALUE_CELL = 'A1'

# Cell containing date range info to use in output filename
DATE_CELL = 'A2'

# Output filename prefix
FILE_PREFIX = 'Meter Reads Data'

# Column width settings dictionary pairs {column: size}
COLUMN_WIDTHS = {'A': 17, 'B': 35, 'C': 27, 'D': 16,
                 'E': 9, 'F': 6, 'G': 28, 'H': 12,
                 'I': 12, 'J': 9, 'K': 14, 'L': 15,
                 'M': 16, 'N': 17}

# Find and replace information to update title cell
REPLACE_VALUE = {'cell': 'A1',
                 'find': 'Read Data Dump',
                 'replace': 'Reads Data'}
