import json


class OpenFile:
    @staticmethod
    def open_file(files):
        """ Load data from JSON"""

        with open(files, 'r', encoding='utf-8') as file:
            return json.load(file)
