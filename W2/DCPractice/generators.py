
def read_lines(filepath, encoding='utf-8'):
    """
    Yield lines from a file one at a time.
    - Strip whitespace from each line
    - Skip empty lines
    - Handle encoding errors gracefully
    
    Usage:
        for line in read_lines('large_file.txt'):
            process(line)
    """
    try:
        with open(filepath, encoding=encoding) as f:
            for line in f:
                if line:
                    cleaned_line = line.strip()
                    yield cleaned_line
    except UnicodeDecodeError as e:
        print("Unable to decode the file")

def batch(iterable, size):
    """
    Yield items in batches of the specified size.
    
    Usage:
        list(batch([1,2,3,4,5,6,7], 3))
        # [[1,2,3], [4,5,6], [7]]
    """

    while(len(iterable)):
        yield iterable[:size]
        iterable = iterable[:size]
    
    
