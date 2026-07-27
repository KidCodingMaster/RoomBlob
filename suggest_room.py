from json_functions import read_json, write_json


def suggest_room():
    json = read_json("rooms.json")

    max_num = 0
    room_num = None

    for i, room in enumerate(json.values()):
        if room["occupied"] is True:
            continue

        if room["avg"] > max_num:
            max_num = room["avg"]
            room_num = str(i + 1)

    return room_num, max_num


def vacate(room_num):
    json = read_json("rooms.json")

    json[room_num]["occupied"] = False

    write_json("rooms.json", json)


def occupy(room_num):
    json = read_json("rooms.json")

    json[room_num]["occupied"] = True

    write_json("rooms.json", json)
