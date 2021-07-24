from copy import copy

from xlclass import COLORS, Xlsx


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


def _highlight_rows(out_xl: Xlsx, startrow: int = 1) -> None:
    """
    Highlights alternating rows starting at startrow until the end of the 
    sheet, unless it hits a row with 'Grand Total' in cell column 'A'.

    Args:
        out_xl (Xlsx): Object containing the cells to highlight
        startrow (int, optional): Row number where highlighting should begin.
        Defaults to 1.
    """
    highlight_row = copy(startrow)
    for row_number, row in enumerate(out_xl.ws.iter_rows(), 1):
        if row_number < startrow:
            continue
        if 'Grand Total' in out_xl.ws[f'A{row_number}'].value:
            break
        if row_number == highlight_row:
            for cell in row:
                cell.fill = COLORS.get('gray')
            highlight_row += 2


def format_cells(out_xl: Xlsx, find_replace: dict, col_settings: dict) -> None:
    """
    Replaces the text in the specified cell with a new value and adjusts
    the width of the cells.

    Args:
        out_xl (Xlsx): Object containing the cell data to adjust.
        find_replace (dict): Dictionary containing the cell location and
        find and replace values. 
        col_settings (dict): {column: value} pairs to use when adjusting
        the size of the specified cells.
    """
    _update_title_cell(out_xl, find_replace)
    _set_column_widths(out_xl, col_settings)
    _highlight_rows(out_xl, startrow=5)
