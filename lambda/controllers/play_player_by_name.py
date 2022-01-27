import json
import ast
import random
from api.http import http

def play_player_by_name(language_prompts, name):

    name_formatted = name.lower().replace(" ", "-")
    player_list = ast.literal_eval(json.loads(http('/prod/players/name/{}'.format(name_formatted))))
    if len(player_list) == 0:
        speech_output = random.choice(language_prompts["PLAYER_NO_EXIST"]).format(name)
    else:
        player_data = player_list[0]
        side = language_prompts["SIDE_TRANSLATE"][0] if player_data["data"]["side"] == "Drive" else language_prompts["SIDE_TRANSLATE"][1]

        speech_output = random.choice(language_prompts["PLAYER_DATA"]).format(
                                                                                    name, 
                                                                                    player_data["position"],
                                                                                    player_data["data"]["score"], 
                                                                                    side,
                                                                                    player_data["data"]["partner"],
                                                                                    player_data["data"]["born_date"],
                                                                                    player_data["data"]["born_place"],
                                                                                    player_data["data"]["height"],
                                                                                    player_data["data"]["home_place"],
                                                                                )
    return speech_output