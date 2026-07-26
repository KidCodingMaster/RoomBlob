from json_functions import write_json


def create_rooms(num_rooms):
    data = {}

    for num in range(num_rooms):
        data[str(num + 1)] = {"reviews": [], "ratings": [], "avg": 0.0}

    write_json("./rooms.json", data)
