import json
def get_all_flags():
    with open('./data/data.json', 'r', encoding='utf-8') as file_:
        countries = json.load(file_)
        continents = list(countries.keys())
    return countries, continents
