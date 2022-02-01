import json
import ast
import random
import unidecode
from api.http import http

def play_player_side(language_prompts, name):

    name_formatted = unidecode.unidecode(name.lower().replace(" ", "-"))
    player_list = ast.literal_eval(json.loads(http('/prod/players/name/{}'.format(name_formatted))))
    if len(player_list) == 0:
        speech_output = random.choice(language_prompts["PLAYER_NO_EXIST"]).format(name)
    else:
        player_data = player_list[0]
        side = language_prompts["SIDE_TRANSLATE"][0] if player_data["data"]["side"] == "Drive" else language_prompts["SIDE_TRANSLATE"][1]
        speech_output = random.choice(language_prompts["PLAYER_SIDE"]).format(name, side)

    return speech_output