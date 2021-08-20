from make_array import bet_size_array, money_invested_villian, money_invested_array
from configuration import position, opponent, context

big_blind_bet_size = 1


small_blind_bet_size = 0.5


bet_size = bet_size_array[0]

num_chip_denominations = 5
chipcount_array = [25, 5, 1, 0.5, 0.1]
chip_stack_size = bet_size

remainder = chip_stack_size
chip_stack_pieces_bet = [0] * 5
current_chip_size = chipcount_array[0]
parition_finished = False
chip_size_index = 0

while not parition_finished:
    chip_stack_pieces_bet[chip_size_index] = int(remainder / current_chip_size)
    remainder = (remainder % current_chip_size)

    if chip_size_index == (num_chip_denominations - 1) or remainder == 0:
        parition_finished = True
    else:
        chip_size_index += 1
        current_chip_size = chipcount_array[chip_size_index]

#####################################################################################################################
num_chip_denominations_big_blind = 5
chipcount_array_big_blind = [25, 5, 1, 0.5, 0.1]
chip_stack_size_big_blind = big_blind_bet_size

remainder_big_blind = chip_stack_size_big_blind
chip_stack_pieces_big_blind = [0] * 5
current_chip_size_big_blind = chipcount_array_big_blind[0]
parition_finished_big_blind = False
chip_size_index_big_blind = 0

while not parition_finished_big_blind:
    chip_stack_pieces_big_blind[chip_size_index_big_blind] = int(remainder_big_blind / current_chip_size_big_blind)
    remainder_big_blind = (remainder_big_blind % current_chip_size_big_blind)

    if chip_size_index_big_blind == (num_chip_denominations_big_blind - 1) or remainder_big_blind == 0:
        parition_finished_big_blind = True
    else:
        chip_size_index_big_blind += 1
        current_chip_size_big_blind = chipcount_array_big_blind[chip_size_index_big_blind]

##################################################################################################################################
num_chip_denominations_small_blind = 5
chipcount_array_small_blind = [25, 5, 1, 0.5, 0.1]
chip_stack_size_small_blind = small_blind_bet_size

remainder_small_blind = chip_stack_size_small_blind
chip_stack_pieces_small_blind = [0] * 5
current_chip_size_small_blind = chipcount_array_small_blind[0]
parition_finished_small_blind = False
chip_size_index_small_blind = 0

while not parition_finished_small_blind:
    chip_stack_pieces_small_blind[chip_size_index_small_blind] = int(remainder_small_blind / current_chip_size_small_blind)
    remainder_small_blind = round((remainder_small_blind % current_chip_size_small_blind),1)

    if chip_size_index_small_blind == (num_chip_denominations_small_blind - 1) or remainder_small_blind == 0:
        parition_finished_small_blind = True
    else:
        chip_size_index_small_blind += 1
        current_chip_size_small_blind = chipcount_array_small_blind[chip_size_index_small_blind]

#############################################################################################################################
num_chip_denominations_villian = 5
chipcount_array_villian = [25, 5, 1, 0.5, 0.1]
chip_stack_size_villian = money_invested_villian

remainder_villian = float(chip_stack_size_villian)
chip_stack_pieces_villian = [0] * 5
current_chip_size_villian = chipcount_array_villian[0]
parition_finished_villian = False
chip_size_index_villian = 0

while not parition_finished_villian:
    chip_stack_pieces_villian[chip_size_index_villian] = int(remainder_villian / current_chip_size_villian)
    remainder_villian = round((remainder_villian % current_chip_size_villian),1)

    if chip_size_index_villian == (num_chip_denominations_villian - 1) or remainder_villian == 0:
        parition_finished_villian = True
    else:
        chip_size_index_villian += 1
        current_chip_size_villian = chipcount_array_villian[chip_size_index_villian]
#########################################################################################################################################
num_chip_denominations_hero = 5
chipcount_array_hero = [25, 5, 1, 0.5, 0.1]
chip_stack_size_hero = money_invested_array

remainder_hero = float(chip_stack_size_hero)
chip_stack_pieces_hero = [0] * 5
current_chip_size_hero = chipcount_array_hero[0]
parition_finished_hero = False
chip_size_index_hero = 0

while not parition_finished_hero:
    chip_stack_pieces_hero[chip_size_index_hero] = int(remainder_hero / current_chip_size_hero)
    remainder_hero = round((remainder_hero % current_chip_size_hero),1)

    if chip_size_index_hero == (num_chip_denominations_hero - 1) or remainder_hero == 0:
        parition_finished_hero = True
    else:
        chip_size_index_hero += 1
        current_chip_size_hero = chipcount_array_hero[chip_size_index_hero]


pot_size = float(small_blind_bet_size) + float(big_blind_bet_size) + float(money_invested_villian) + float(money_invested_array)
pot_odds = (bet_size/(pot_size + bet_size))*100
hero_chip_amount = (100-bet_size)

initial_investments = [0.5, 1, 0, 0, 0, 0]
initial_investments[int(int(position)-1)] = float(money_invested_array)

if context != '1':
    initial_investments[int(int(opponent)-1)] = float(money_invested_villian)


