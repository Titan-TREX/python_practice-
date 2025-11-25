import json

game_data = {
    "player": "Ali",
    "level": 5,
    "score": 1200
}

with open("game_data.json", "w") as file:
    json.dump(game_data, file, indent=4)
print("Game data saved to game_data.json")
game_data = json.load(open("game_data.json"))
print(game_data)