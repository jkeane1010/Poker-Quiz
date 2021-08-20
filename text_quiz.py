import pyodbc
from datetime import datetime
from getting_cards import hero_cards_array
from getting_chip_stacks import chip_stack_pieces_bet, chip_stack_pieces_big_blind, chip_stack_pieces_small_blind, pot_odds, hero_chip_amount
from configuration import questions, hero_name
from getting_options import possible_answers
from make_array import bet_size_array, pot_size_array, money_invested_array, easiness_array, action_array
from info_from_db import scenario_text, scenario
from getting_dealer import dealer
from getting_players_folded import players_folded, next_to_act

quiz_number = 1

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jadam\OneDrive\Documents\Poker_Ranges.accdb;')  # Connects to the databse
cursor = conn.cursor()


correct_answers = 0
i = 0

while i < questions:
    query1 = 'SELECT TOP 1 Questions.Quiz, Questions_1.ID FROM Questions, Questions AS Questions_1 ORDER BY Questions.Quiz DESC , Questions_1.ID DESC;'
    cursor.execute(query1)  # Finds the number of scores already in the databse

    for row in cursor.fetchall():
        ID = (row[1] + 1)
    print('Question: ', (i+1), '/', questions)
    print('Correct answers: ', correct_answers, '/', i)
    print('Cards Dealt:' ' ', hero_cards_array[i][0], 'and'  ' ', hero_cards_array[i][1])
    print('Scenario:' ' ', scenario_text)
    print('The dealer is in the' ' ', dealer)
    print('Next to Act: ', next_to_act)
    print('Players Folded: ', players_folded)
    print('Bet size:' ' ', bet_size_array[i])
    print('Chip Stack:' ' ', chip_stack_pieces_bet)
    print('You have ', hero_chip_amount, 'BB')
    print('Big Blind Bet Size:' ' ', round(((pot_size_array[i]*2)/3), 1))
    print('Big Blind Chip Stack:' ' ', chip_stack_pieces_big_blind)
    print('Small Blind Bet Size:' ' ', round(((pot_size_array[i] * 1) / 3), 1))
    print('Small Blind Chip Stack:' ' ', chip_stack_pieces_small_blind)
    print('Pot odds:' ' ', "{:.2f}".format(pot_odds), '%')
    print('Money already invested during hand:' ' ', money_invested_array)
    print('Easiness Rating:' ' ', easiness_array[i])
    print('Possible Answers:', possible_answers)
    answer = input('Please Enter what Action you would take: ')

    if answer == action_array[i]:
        correct_answers += 1
        score_ID = 100
        print("Well done that's right")
        print('Your Score was: ', score_ID)
        print('........................................................')
        question_score = (ID, quiz_number, hero_name, datetime.now(), easiness_array[i], scenario, (hero_cards_array[i][0] + hero_cards_array[i][1]), action_array[i], bet_size_array[i], True, score_ID, 'None')  # Adds this score to the database
        cursor.execute('INSERT INTO Questions VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', question_score)
        conn.commit()
        i += 1



    elif answer != action_array[i]:
        scoreID = (10 - (int(easiness_array[i])))
        score_ID = scoreID * 10
        print("Sorry That's wrong")
        print('The correct answer is ', action_array[i])
        print('Your Score was: ', score_ID)
        print('........................................................')
        question_score = (ID, quiz_number, hero_name, datetime.now(), easiness_array[i], scenario, (hero_cards_array[i][0] + hero_cards_array[i][1]), action_array[i], bet_size_array[i], False, score_ID, 'None')  # Adds this score to the database
        cursor.execute('INSERT INTO Questions VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', question_score)
        conn.commit()
        i += 1

print('Done')
