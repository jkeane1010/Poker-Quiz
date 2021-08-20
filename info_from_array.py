from make_array import hands_array
from configuration import questions

i = 0
cards_array = []*questions
type_array = []*questions
action_array = []*questions
easiness_array = []*questions
pot_size_array = []*questions
bet_size_array = []*questions
money_invested_array = []*questions

while i < questions:
    cards_array[i] = hands_array[i][0]
    type_array[i] = hands_array[i][1]
    action_array[i] = hands_array[i][2]
    easiness_array[i] = hands_array[i][3]
    pot_size_array[i] = float(hands_array[i][4])
    bet_size_array[i] = float(hands_array[i][5])
    money_invested_array[i] = hands_array[i][6]
    i += 1