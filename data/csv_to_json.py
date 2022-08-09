import csv, json


# Params
csv_file_ads = 'ads.csv'
json_file_ads = '../fixtures/ads.json'
ads_model = 'ads.ad'

csv_file_catetories = 'categories.csv'
json_file_categories = '../fixtures/categories.json'
categories_model = 'ads.category'


# Function
def csv_to_json(csv_file_path: str, json_file_path: str, model: str) -> str:
    """Convert csv to json"""

    # read csv file and add to dictionary
    with open(csv_file_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data: list = [
            {'model': model,
             'pk': int(row['id']),
             'fields': row
             }
            for row in reader
        ]

    # create new json file and write data
    with open(json_file_path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

    return f'Data from csv ({csv_file_path}) converted to json ({json_file_path})'


if __name__ == '__main__':
    print(csv_to_json(csv_file_ads, json_file_ads, ads_model))
    print(csv_to_json(csv_file_catetories, json_file_categories, categories_model))
