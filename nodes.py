"""
CreateNodes:
    1. Created fieldnames and rows of dataset on intitialization
    2. Creates a csv file when class is called
    3. get_data: to access the created data
    4. print_data: logs the created data on the console
"""

import csv

class CreateNodes:

    FIELD_NAMES = None
    ROWS = None

    def __init__(self, fieldnames, rows):
        """
        Document
        """
        self.FIELD_NAMES = fieldnames
        self.ROWS = rows

    def __call__(self, save_path, file_name):
        """
        Document
        """
        file_path = save_path + file_name
        with open(file_path, "w") as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerow(self.FIELD_NAMES)
            csvwriter.writerows(self.ROWS)
    
    def get_data(self):
        """
        Return a list of list that will be written in csv when the class is called
        """
        field = self.FIELD_NAMES
        rows = self.ROWS
        data = [field] + rows
        return data

    def print_data(self):
        """
        prints data that will be written in csv when the class is called
        """
        data = self.get_data()
        for row in data:
            print(row)

    # Further tasks for later development
    # TODO: Incorporate build_artists_titles_list function from utility_function
