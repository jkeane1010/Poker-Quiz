from info_from_db import row2
from configuration import questions

w, h = (8, questions)
hand_list = [['' for i in range (w)] for j in range(h)]

cards_array = ['']*questions
type_array = ['']*questions
action_array = ['']*questions
easiness_array = ['']*questions
pot_size_array = ['']*questions
bet_size_array = ['']*questions
money_invested_array = ['']*questions

x = 0
while x < questions:
    exec(open('info_from_db.py').read())
    hand_list[x] = [elem for elem in row2]
    x += 1

hands_array = (hand_list[1])

z = 0
while z < questions:
    cards_array[z] = hands_array[z][0]
    type_array[z] = hands_array[z][1]
    action_array[z] = hands_array[z][2]
    easiness_array[z] = hands_array[z][3]
    pot_size_array[z] = float(hands_array[z][4])
    bet_size_array[z] = float(hands_array[z][5])
    money_invested_array = hands_array[0][6]
    money_invested_villian = hands_array[0][7]
    z += 1
