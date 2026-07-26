import json


def write_json(file, data):
    with open(file, "w") as f:
        json.dump(data, (f))


def read_json(file):
    with open(file, "r") as f:
        return json.load(f)
