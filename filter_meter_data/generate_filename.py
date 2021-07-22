# Generate output filename

from pathlib import Path

def get_filepath(folder: str, prefix: str, suffix: str) -> Path:
    
    return Path(f'{folder}/{prefix}, {suffix}.xlsx')
