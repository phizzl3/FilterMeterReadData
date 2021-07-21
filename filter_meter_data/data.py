# Variables

from pathlib import Path


# Source file search expression
SOURCE_FILENAME = r'Meter_Reads_Data_Dump.*\.xlsx'

# Folder to search for source files (User's Downloads folder)
FOLDER = Path().home().resolve() / "Downloads"

# Columns from source file containing the needed info
KEEP_COLUMNS = ('A', 'B', 'C', 'D', 'E', 'F', 'H', 
                'J', 'K', 'N', 'P', 'BF', 'BK', 'CC')

# Value to verify to check that we're using the correct source file
CHECK_VALUE = 'Meter Read Data Dump'

# Cell to verify info for CHECK_VALUE
VALUE_CELL = 'A1'

# Cell containing date range info
DATE_CELL = 'A2'
