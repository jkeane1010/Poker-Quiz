from info_from_db import scenario
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jadam\OneDrive\Documents\Poker_Ranges.accdb;')  # Connects to the databse
cursor = conn.cursor()
query4 = f"SELECT possible_answers.NumberofOptions, possible_answers.Option1, possible_answers.Option2, possible_answers.Option3, possible_answers.Option4, possible_answers.Option5, possible_answers.Option6 FROM possible_answers WHERE (((possible_answers.Scenario)={scenario}));"
cursor.execute(query4) #Gets all the possible answers for that sceanrio, 3 possible answers for opening, 6 possibles answers for 5 Betting

for row in cursor.fetchall():
    number_of_answers = row[0]
    possible_answers_ID = row[1:(number_of_answers+1)]

possible_answers = ['']*number_of_answers

i = 0
while i < (number_of_answers):
    query5 = f"SELECT Options.ShortText FROM Options WHERE (((Options.ID)={possible_answers_ID[i]}));"
    cursor.execute(query5) #Finds the word version of the possible answer
    for row3 in cursor.fetchall():
        option = str(row3[0])
        possible_answers[i] = option #Saves the word versions of all possible answers in an array
    i += 1

csr = conn.cursor()
csr.close()
conn.close()

