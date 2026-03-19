from .exceptions import *
from .file_logger import setup_logger

def read_csv_file(filepath):
    """
    Read a CSV file and return a list of dictionaries.
    
    Should handle:
    - FileNotFoundError
    - UnicodeDecodeError (try utf-8, then latin-1)
    - Empty files
    
    Returns: List of dictionaries (one per row)
    Raises: FileProcessingError with descriptive message
    """
    
    records = []

    with open(filepath, 'r', encoding='utf-8') as f:
        if not f:
            
            return []
        
        for i, line in enumerate(f):
            entry = line.split(',')
            print(entry)

    