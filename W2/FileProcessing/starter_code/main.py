from .util.file_reader import read_csv_file
from .util.file_logger import setup_logger

def main():
    logger = setup_logger(__name__)
    file_path = "sample.csv"
    try:
        read_csv_file("")
    except FileNotFoundError as e:
        logger.warning(f"No file found: {e}")
        
        print(f"No file found: {e}")

    
        
    pass


if __name__ == "__main__":
    main()