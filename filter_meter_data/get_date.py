# Get formatted date range from source file

from xlclass import Xlsx


def get_date(xl: Xlsx, cell: str) -> str:
    
    # Get date range and return formatted string
    date = xl.ws[cell].value
    date = date.strip('Date Range: ')
    date = date.replace('/', '.')
    date = date.replace(' ', '')
    
    return date
