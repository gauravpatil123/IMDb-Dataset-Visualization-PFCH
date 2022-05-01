"""
DatasetPreprocessing:
    1. Sets dataset paths at initialization
    2. Creates a python dictionary from the tsv datafiles when class is called
    3. Saves the created python dictionary to a json file with save_data function
"""

import csv
import json

class DatasetProcessing:

    DATA = {}
    READER = None
    HEADERS = None
    dataset_path = None

    def __init__(self, base_dir, dataset):
        """
        Initializes dataset_path by combining friectory and filename
        """
        self.dataset_path = base_dir + dataset

    def __call__(self, pop_index=0):
        """
        Returns a data dictionary created from the tsv file of the original dataset
        """
        with open(self.dataset_path, "r") as file_handle:
            self.READER = csv.DictReader(file_handle, delimiter="\t")
            self.HEADERS = self.READER.fieldnames
            data = {}
            headers = list(self.HEADERS)
            # initializing key_header from header list # default index = 0
            key_header = headers.pop(pop_index)
            for row in self.READER:
                id = row[key_header]
                data[id] = {}
                for header in headers:
                    key = str(header)
                    value = row[header]
                    # logic for NoneType values
                    if value == None:
                        value = ""
                    # logic to handle multiple values
                    if value.find(',') != -1:
                        data[id][key] = list(value.split(','))
                    else:
                        data[id][key] = row[header]
            self.DATA = data

    def save_data(self, save_path, file_name_ext):
        """
        Saves the dictionary constructed in class call to a json file
        Using save_path and *file_name.json
        """
        data = self.DATA
        json.dump(data, open(save_path + file_name_ext, 'w'), indent=4)

