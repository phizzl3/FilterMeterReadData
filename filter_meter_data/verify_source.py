# Check source file for correct info

from xlclass import Xlsx


def verify_value(xl: Xlsx, val: str, cell: str) -> bool:
    
    # Verify that the data in the passed cell matches the 
    # value we're looking for.
    return xl.ws[cell].value == val
