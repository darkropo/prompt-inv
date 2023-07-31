import csv
import json
import os

def convert_csv_to_json():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory) 
    csv_file_path = os.path.join(parent_directory, 'static', 'files', 'data.csv')
    json_file_path = os.path.join(parent_directory, 'static', 'files', 'data.json')

    data = {}

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        field_names = next(csv_reader)
        for row in csv_reader:
            data_row = {}
            for index, value in enumerate(row):
                data_row[field_names[index]] = value
            data[row[0]] = data_row

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print("CSV file converted to JSON successfully!")