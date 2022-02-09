import json


def load_database(src_file='products_db.json'):
    with open(src_file, 'r') as file_obj:
        data = json.load(file_obj)
    return data