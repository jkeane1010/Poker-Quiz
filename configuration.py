import pyodbc

hero_name = input('Please enter your username: ')
position = input('Please enter your position on the table: ')
context = input('Please enter the context of the quiz (1 for Opening, 2 for 3Betting etc): ')
opponent = input('Please enter the position of your opponent (7 if you are opening): ')
questions_input = input('Please enter how many questions you want: ')
questions = int(questions_input)

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jadam\OneDrive\Documents\Poker_Ranges.accdb;')  # Connects to the databse
cursor = conn.cursor()
query = f"SELECT Positions.LongName FROM Positions WHERE (((Positions.ID)={position}));"
cursor.execute(query)
for row in cursor.fetchall():
        player = row[0] #Finds the word version of the player position from the database
                        # E.g 1 is 'Small Blind'

query2 = f"SELECT Positions.LongName FROM Positions WHERE (((Positions.ID)={opponent}));"
cursor.execute(query2)
for row2 in cursor.fetchall():
        villian = row2[0] #Finds the word version of the villian position from the database

csr = conn.cursor()
csr.close()
conn.close()