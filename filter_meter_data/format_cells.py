from xlclass import Xlsx


def _update_title_cell(out_xl: Xlsx, find_replace: dict) -> None:
    """
    Replaces the text in the specified cell with a new value.

    Args:
        out_xl (Xlsx): Object containing the values to replace.
        find_replace (dict): Dictionary containing the cell location and
        find and replace values.
    """
    out_xl.ws[
        find_replace['cell']] = out_xl.ws[find_replace['cell']].value.replace(
        find_replace['find'], find_replace['replace'])


def _set_column_widths(out_xl: Xlsx, col_settings: dict) -> None:
    """
    Uses a dictionary of columns and values to set the width of the cells.

    Args:
        out_xl (Xlsx): Object containing the cells to adjust.
        col_settings (dict): {column: value} pairs to use when adjusting
        the size of the specified cells.
    """
    out_xl.set_cell_size(col_settings)


def _highlight_rows(out_xl: Xlsx) -> None:
    """
    Highlights alternating rows from row 5 up to row 166.
    
    Args:
        out_xl (Xlsx): Object containing the cells to highlight
    """
    out_xl.highlight_rows(startrow=5, stoprow=166, alternate=True)


def _set_bold_rows(out_xl: Xlsx) -> None:
    """
    Sets all cells to bold beginning at startrow and ending 
    just before stoprow.

    Args:
        out_xl (Xlsx): Object containing the cells to set as bold.
    """
    out_xl.set_bold_rows(startrow=1, stoprow=5)


def _total_combined_meters(out_xl: Xlsx, startrow: int = 5) -> None:
    """
    Adds up the last row and sets the final amount to the last cell in 
    the column.

    Args:
        out_xl (Xlsx): Object containing the amounts to be totaled. 
        startrow (int, optional): Row number to start adding. Defaults to 5.
    """
    total_meter = 0
    for row_number, row in enumerate(out_xl.ws.iter_rows(), 1):
        if row_number < startrow:
            continue
        if 'Grand Total' in out_xl.ws[f'A{row_number}'].value:
            out_xl.ws[f'N{row_number}'] = total_meter
            break
        total_meter += out_xl.ws[f'N{row_number}'].value


def format_cells(out_xl: Xlsx, find_replace: dict, col_settings: dict) -> None:
    """
    Updates the title cell, sets the column widths, sets the top rows
    to bold, highlights alternating rows of data in gray, and adds and
    inserts the total meters at the bottom.

    Args:
        out_xl (Xlsx): Object containing the cell data to adjust.
        find_replace (dict): Dictionary containing the cell location and
        find and replace values. 
        col_settings (dict): {column: value} pairs to use when adjusting
        the size of the specified cells.
    """
    _update_title_cell(out_xl, find_replace)
    _set_column_widths(out_xl, col_settings)
    _highlight_rows(out_xl)
    _set_bold_rows(out_xl)
    _total_combined_meters(out_xl)
