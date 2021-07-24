#!/usr/bin/env python3

import warnings
from time import sleep

import dropfile
from format_cells import format_cells
from get_date import get_date
from get_filepath import get_filepath
from re_file_search import get_list
from user_values import (CHECK_VALUE, COLUMN_WIDTHS, DATE_CELL, FILE_PREFIX,
                         FOLDER, KEEP_COLUMNS, REPLACE_VALUE, SOURCE_FILENAME,
                         VALUE_CELL)
from verify_value import verify_value
from write_cells import write_cells
from xlclass import Xlsx


def get_files_together():
    # Get list of source files from folder
    source_files = get_list(FOLDER, SOURCE_FILENAME)

    # Ask for file location if none are found (single list item)
    if not source_files:
        source_files = [dropfile.get()]
    return source_files


def process_the_files(source_files):
    # Process each located file
    for file in source_files:
        # Generate objects
        source_xl = Xlsx(file)
        target_xl = Xlsx()

        # Check source for correct contents
        if not verify_value(source_xl, CHECK_VALUE, VALUE_CELL):
            continue

        # Get formatted dates and generate output filepath
        date_range = get_date(source_xl, DATE_CELL)
        out_file_path = get_filepath(
            FOLDER, FILE_PREFIX, date_range)

        # Write and format the cells/values
        write_cells(source_xl, target_xl, KEEP_COLUMNS)
        format_cells(target_xl, REPLACE_VALUE, COLUMN_WIDTHS)

        # Save the output file and display message
        target_xl.save(out_file_path)
        print(f"\nFile written to:\n{out_file_path}")


if __name__ == '__main__':
    # Ignore openpyxl style warning
    warnings.simplefilter('ignore')

    # Get and process files
    source_files = get_files_together()
    process_the_files(source_files)
    sleep(2)
