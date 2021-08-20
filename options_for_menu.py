import json

hand_stages = [['Pre-Flop', 1, 1], ['Flop', 0, 0], ['Turn', 0, 0], ['River', 0, 0]]
hero_positions = [['Small Blind', 0, 1], ['Big Blind', 0, 1], ['Under The Gun', 0, 1], ['HiJack', 0, 1], ['Cut-Off', 0, 1], ['Button', 0, 1]]
scenario_options = [['Open', 1, 1], ['3Bet', 0, 1], ['4Bet', 0, 1], ['5Bet', 0, 1]]
villain_position = [['Small Blind', 0, 1], ['Big Blind', 0, 1], ['Under The Gun', 0, 1], ['HiJack', 0, 1], ['Cut-Off', 0, 1], ['Button', 0, 1]]
no_of_questions = [['5', 0, 1], ['10', 0, 1], ['20', 1, 1], ['50', 0, 1], ['100', 0, 1]]
menu_options = {'Hand Stage': hand_stages, 'Hero Position': hero_positions, 'Scenario Option': scenario_options, 'Villain Position': villain_position, 'Number of Questions': no_of_questions}

print(menu_options)

json_menu_options = json.dumps(menu_options)
