import json
import ast
from api.http import http

def play_top_ranking(language_prompts, number_input):

    number = int(number_input)
    ranking_list = json.loads(http('/prod/players/ranking'))
    sorted_ranking_list = sorted(ast.literal_eval(ranking_list), key=lambda k: k['position'], reverse=False)[0:number]
    speech_output = language_prompts["TOP_RANKING"][0].format(number) if number < 2 else language_prompts["TOP_RANKING"][1].format(number)
    speech_output+=f'{sorted_ranking_list[0]["name"].replace("-", " ").title()}'

    for player in sorted_ranking_list[1:(len(sorted_ranking_list)-1)]:
        player_name = player["name"].replace("-", " ").title()
        speech_output+=f', {player_name} \r\n'
    
    if len(sorted_ranking_list)>1:
        speech_output+=f'y {sorted_ranking_list[len(sorted_ranking_list)-1]["name"].replace("-", " ").title()} \r\n'

    return speech_output