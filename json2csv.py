import csv
import json
import os


def json_to_csv(json_file):

    with open(json_file, 'r') as f:
        data = json.load(f)

    # Записываем данные в CSV
    with open(f'{json_file}.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

json_to_csv("example.json")