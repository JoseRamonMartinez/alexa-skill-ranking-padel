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
        speech_output = random.choice(language_prompts["PLAYER_EXIST"]).format(name, data["position"], data["score"], data["won_matches"])

    return speech_output