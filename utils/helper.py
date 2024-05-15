import os
from csv import DictReader


def get_csv_data_from_file(filename: str):
    file_full_name = os.path.join('../data', filename)
    if os.path.exists(file_full_name):
        with open(file_full_name) as f:
            yield list(DictReader(f))