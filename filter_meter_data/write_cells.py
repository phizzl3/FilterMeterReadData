from string import ascii_uppercase

from xlclass import Xlsx


def write_cells(in_xl: Xlsx, out_xl: Xlsx, cols: list) -> None:
    """
    Writes the specified column data from the source Xlsx object to 
    the target Xlsx object in the order passed.

    Args:
        in_xl (Xlsx): Source object to read data from.
        out_xl (Xlsx): Target object to write data to.
        cols (list): List of (str) column letters containing the data
        to be copied.
    """
    # Generates a dictionary of {source column: target column} using cols
    # as source and ascii letters as target and then writes values.
    columns = {src: target for src, target in zip(cols, ascii_uppercase)}
    out_xl.copy_sheet_data(in_xl, columns)
