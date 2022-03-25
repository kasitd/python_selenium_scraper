import csv
import os
from datetime import date


def write_into_csv_file(offer_list):
    file_name = f'raw_data{date.today().strftime("%d_%m_%Y")}.csv'
    try:
        with open(file_name, mode='w+', newline='', encoding='utf8') as raw_csv_file:
            filds = ['Job_title',
                     'Employer',
                     'City',
                     'Contract',
                     'Position',
                     'Mode',
                     'Recrutation',
                     'Required_technologies',
                     'Optional_technologies',
                     'Responsibilities',
                     'Requirement']
            file_writer = csv.writer(raw_csv_file)
            file_writer.writerow(filds)
            file_writer.writerows(offer_list)
    except FileNotFoundError:
        print("Output file not present", 'raw_data.csv')
        print("Current dir: ", os.getcwd())
        raise FileNotFoundError