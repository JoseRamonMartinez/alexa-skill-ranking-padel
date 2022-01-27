import json
import ast
import random
from api.http import http

def play_player_by_position(language_prompts, number_input):

    number = int(number_input)

    ranking_list = ast.literal_eval(json.loads(http('/prod/players/ranking/{}'.format(number))))
    speech_output = language_prompts["TOP_PLAYER"][len(ranking_list)-1].format(number)

    for player in ranking_list:
        speech_output+=player["name"].replace("-", " ").title()
        speech_output += random.choice(language_prompts["CONNECTOR"]) if (len(ranking_list)>1) and (player == ranking_list[0]) else ""
        
    if len(ranking_list) == 0:
        speech_output = random.choice(language_prompts["DRAW"]).format(number, number-1)

    return speech_output