from time import sleep

from xlclass import Xlsx


def verify_value(xl: Xlsx, val: str, cell: str) -> bool:
    """
    Verifies that the passed value in specified cell matches what is 
    expected to be used before running the remaining steps.

    Args:
        xl (Xlsx): Object containing the data to be verified.
        val (str): Value that will be used to compare against the specified
        cell's value.
        cell (str): Cell containing the value to be compared.

    Returns:
        bool: T/F value based on whether or not the values match.
    """
    if xl.ws[cell].value == val:
        return True
    print(f"\nFile contents don't match for:\n{xl.path}\nPlease verify.\n")
    sleep(2)
