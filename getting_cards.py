import pyodbc
from make_array import cards_array, type_array
from configuration import  questions
exec(open('info_from_db.py').read())


w, h = (2, questions)
hero_cards_array = [['' for i in range (w)] for j in range(h)] #Creates a 2D array so there is a seperate array of 2 cards for every question

z = 0
while z < questions:
    if type_array[z] == 'Suited': #If the cards are suites they have the same suit
        suit_1 = 'h'
        suit_2 = 'h'

    elif type_array[z] == 'Offsuit' or type_array[z] == 'Pair': #If the cards are pairs or offsuit they get different suits
        suit_1 = 'd'
        suit_2 = 'c'

    hero_cards_array[z][0] = (cards_array[z][0] + suit_1) #Combines the value of the card with the suit to get the full card name
    hero_cards_array[z][1] = (cards_array[z][1] + suit_2)
    z += 1 #Contines getting 2 random cards for every question

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jadam\OneDrive\Documents\Poker_Ranges.accdb;')  # Connects to the databse
cursor = conn.cursor()

#print(cards_array[0])
hole_cards = ['']*questions

i = 0
while i < questions:
    query = f"SELECT HoleCards.ID FROM HoleCards WHERE (((HoleCards.ShortName)='{cards_array[i]}'));"
    cursor.execute(query)  # Gets the correct scenario
    for row in cursor.fetchall():
        hole_cards[i] = row[0]
    i += 1

#print(hole_cards)