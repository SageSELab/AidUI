import json

def write_json_file(dict):
    with open('textual_ranking.json', 'w') as fp:
        json.dump(dict, fp)
