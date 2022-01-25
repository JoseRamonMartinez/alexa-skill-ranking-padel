import json
import random
import ast
from api.http import http

def play_ranking(language_prompts):
    ranking_list = json.loads(http('/prod/players/ranking'))

    sorted_ranking_list = sorted(ast.literal_eval(ranking_list), key=lambda k: k['position'], reverse=False)[0:3]

    speech_output = random.choice(language_prompts["RANKING"])

    speech_output+=sorted_ranking_list[0]["name"].replace("-", " ").title() + ', '
    speech_output+=sorted_ranking_list[1]["name"].replace("-", " ").title() + ' y '
    speech_output+=sorted_ranking_list[2]["name"].replace("-", " ").title()

    return speech_output