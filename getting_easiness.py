import pyodbc
from getting_cards import hole_cards
from getting_options import number_of_answers, possible_answers_ID
from info_from_db import scenario
from configuration import questions

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jadam\OneDrive\Documents\Poker_Ranges.accdb;')  # Connects to the databse
cursor = conn.cursor()

i = 0
optionset_ID = ['']*(number_of_answers) #creates an empty array with a cell for every answer

while i < number_of_answers:
    query = f"SELECT OptionSets.ID FROM OptionSets WHERE (((OptionSets.Scenario)={scenario}) AND ((OptionSets.Option)={possible_answers_ID[i]}));"
    cursor.execute(query)  # Gets the correct scenario
    for row in cursor.fetchall():
        optionset_ID[i] = row[0] #Fills the empty array with the ID for the possible answers. E.g [Fold, Raise, Call] would be [8, 3, 1]
    i += 1

w, h = (number_of_answers, questions)
easiness_ratings_array = [['' for i in range(w)] for j in range(h)] #Creates a 2D array so there can be a seperate array of easiness ratings for every question


z = 0
while z < questions:
    y = 0
    while y < number_of_answers:
        query1 = f"SELECT ActionScores.Easiness FROM ActionScores WHERE (((ActionScores.HoleCards)={hole_cards[z]}) AND ((ActionScores.OptionSet)={optionset_ID[y]}));"
        cursor.execute(query1)  # This searches the database for the easiness rating associated with the hand given in that scenario
        for row1 in cursor.fetchall():
            easiness_ratings_array[z][y] = row1[0]
        y += 1
    z += 1
