from pathlib import Path


def get_filepath(folder: str, prefix: str, suffix: str) -> Path:
    """
    Uses the passed values to generate a formatted filepath in the format:
    "folder/prefix, suffix.xlsx"

    Args:
        folder (str): Target folder path.
        prefix (str): First portion of the output filename.
        suffix (str): Second portion of the output filename.

    Returns:
        Path: Path object representing the formatted filepath.
    """
    return Path(f'{folder}/{prefix}, {suffix}.xlsx')
