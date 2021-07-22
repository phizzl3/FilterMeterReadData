# Check source file for correct info

from xlclass import Xlsx
from time import sleep

def verify_value(xl: Xlsx, val: str, cell: str) -> bool:
    
    # Verify that the data in the passed cell matches the 
    # value we're looking for.
    if xl.ws[cell].value == val:
        return True
        
    print(f"File contents don't match for:\n{file}\nPlease verify.")
    sleep(2)
            
