import json

from make_array import *
from info_from_db import *
from getting_players_folded import *
from getting_chip_stacks import *
from getting_options import *
from getting_cards import *
from making_matrix import *
from gettings_scores import *

w, h = (22, questions)
question_set = [['' for i in range (w)] for j in range(h)]

i = 0
while i < questions:
    question_set[i] = {'Cards': hero_cards_array[i], 'Scenario': scenario_text, 'Hero Bets': float(bet_size_array[i]), 'Next to Act': next_to_act, 'Players Active': players_active, 'Possible answers': possible_answers, 'Correct answer': action_array[i], 'Easiness ratings': easiness_ratings_array[i], 'Hero Place': position, 'Money Invested by Players': initial_investments}
    i += 1

json_question_set = json.dumps(question_set)

x = 0
while x < 14:
    print(matrix[x])
    x += 1
#print((json_question_set))

