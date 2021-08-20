import json
import pyodbc
from info_from_db import scenario
from configuration import context

matrix = [['', 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'],
          ['A', '', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'], #This is the initial matrix
          ['K', 'o', '', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'], # 's' means the cards are the same suit
          ['Q', 'o', 'o', '', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'], # 'o' means the cards are different suits
          ['j', 'o', 'o', 'o', '', 's', 's', 's', 's', 's', 's', 's', 's', 's'], # ' ' means it is a pair
          ['T', 'o', 'o', 'o', 'o', '', 's', 's', 's', 's', 's', 's', 's', 's'],
          ['9', 'o', 'o', 'o', 'o', 'o', '', 's', 's', 's', 's', 's', 's', 's'],
          ['8', 'o', 'o', 'o', 'o', 'o', 'o', '', 's', 's', 's', 's', 's', 's'],
          ['7', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '', 's', 's', 's', 's', 's'],
          ['6', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '', 's', 's', 's', 's'],
          ['5', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '', 's', 's', 's'],
          ['4', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '', 's', 's'],
          ['3', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '', 's'],
          ['2', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', '']]

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jadam\OneDrive\Documents\Poker_Ranges.accdb;')  # Connects to the databse
cursor = conn.cursor()

i = 1
while i <= 13:
    j = 1
    while j <= 13:
        if matrix[i][j] == 'o': #These if and else statements are to make sure that the larger number always comes first when searching the database for the card
            hand = str(matrix[0][j] + matrix[i][0] + matrix[i][j])
        else:
            hand = str(matrix[i][0] + matrix[0][j] + matrix[i][j])

        query = f"SELECT Options.ShortText FROM (ActionScores INNER JOIN ((OptionSets INNER JOIN Options ON OptionSets.Option = Options.ID) INNER JOIN Scenarios ON OptionSets.Scenario = Scenarios.ID) ON ActionScores.[OptionSet] = OptionSets.ID) INNER JOIN HoleCards ON ActionScores.HoleCards = HoleCards.ID WHERE (((HoleCards.ShortName)='{hand}') AND ((OptionSets.Scenario)={scenario}) AND ((ActionScores.Correct)=True));"
        cursor.execute(query) #This searches for the correct answer for that hand in the scenario picked by the user
        for row in cursor.fetchall():
            matrix[i][j] = row[0]
        if context != '1':  #This will leave hands that don't show up in further down scenarios as empty, I.e you will not get 72o in a 4Bet because you already would have folded
            if matrix[i][j] == 's' or matrix[i][j] == 'o' or matrix[i][j] == '':
                matrix[i][j] = 'x'
        if context == '1':
            if matrix[i][j] == 's' or matrix[i][j] == 'o' or matrix[i][j] == '':
                matrix[i][j] = 'F'
        j += 1
    i += 1


x = 0
while x < 14:
    print(matrix[x])
    x += 1

json_matrix = json.dumps(matrix)