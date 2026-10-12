import pandas as pd

"""
 function that takes a path to a csv file as an argument, writes the
 dimensions of the data set and returns the data.
"""


def load(path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(path)
        rows, cols = data.shape
        print(f"Loading dataset of dimensions ({rows}, {cols}) ")
        return data
    except Exception as e:
        print(f" An error occurred: {e}")
        return pd.DataFrame()
