import os
from csv import DictReader


def get_csv_data_from_file(filename: str):
    """
    The function `get_csv_data_from_file` reads a CSV file and yields its contents as a list of
    dictionaries.
    
    :param filename: The `filename` parameter is a string that represents the name of the CSV file from
    which you want to retrieve data
    :type filename: str
    """
    file_full_name = os.path.join('../data', filename)
    if os.path.exists(file_full_name):
        with open(file_full_name) as f:
            yield list(DictReader(f))