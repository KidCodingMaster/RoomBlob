from json_functions import read_json, write_json
from textblob import TextBlob


def give_review(room, review):
    json = read_json("rooms.json")
    rating = TextBlob(review).sentiment.polarity

    json[room]["ratings"].append(rating)
    json[room]["reviews"].append(review)

    json[room]["avg"] = sum(json[room]["ratings"]) / len(json[room]["ratings"])

    write_json("rooms.json", json)
