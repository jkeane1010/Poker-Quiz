from configuration import *


if context == '1':
    if position == '1':
        players_active = [1, 1, 0, 0, 0, 0] #0 means folded, 1 means active
        next_to_act = 'Big Blind'
    elif position == '2':
        players_active = [0, 1, 0, 0, 0, 0]
        next_to_act = 'Under the Gun'
    elif position == '3':
        players_active = [1, 1, 1, 1, 1, 1]
        next_to_act = 'Hijack'
    elif position == '4':
        players_active = [1, 1, 0, 1, 1, 1]
        next_to_act = 'Cut-Off'
    elif position == '5':
        players_active = [1, 1, 0, 0, 1, 1]
        next_to_act = 'Button'
    elif position == '6':
        players_active = [1, 1, 0, 0, 0, 1]
        next_to_act = 'Small Blind'
else:
    players = [0, 0, 0, 0, 0, 0]
    players[int(int(position) - 1)] = 1
    players[int(int(opponent) - 1)] = 1 #All players are folded except the user and the opponent
    players_active = players

    next_to_act = villian

