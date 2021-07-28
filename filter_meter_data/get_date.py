from xlclass import Xlsx


def get_date(xl: Xlsx, cell: str) -> str:
    """
    Gets the date range from the specified cell and strips unused
    characters before returning a new string.

    Args:
        xl (Xlsx): Object containing the date range value.
        cell (str): Cell location containing the date range value. ex: 'A1'

    Returns:
        str: Formatted string of date ranges.
    """
    date = xl.ws[cell].value
    date = date.strip('Date Range: ')
    date = date.replace('/', '.')
    date = date.replace(' ', '')
    
    return date
