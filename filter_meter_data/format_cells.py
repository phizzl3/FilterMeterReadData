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
