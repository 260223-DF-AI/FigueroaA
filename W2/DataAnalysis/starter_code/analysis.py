import pandas as pd

def load_data(filepath):
    """
    Load the orders dataset.
    - Parse dates correctly
    - Handle missing values
    - Return a clean DataFrame
    """
    df = pd.read_csv(filepath)
    print(df.isnull())
    df_filled = df.fillna(-1)
    #print(df.head())

    return

def explore_data(df):
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    pass