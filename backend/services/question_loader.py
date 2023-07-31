import json


def load_questions(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)

    return data['questions']
