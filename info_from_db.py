from configuration import *
import pyodbc

difficulty = 0 #Any hand


conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\jadam\OneDrive\Documents\Poker_Ranges.accdb;')  # Connects to the databse
cursor = conn.cursor()
query = f"SELECT Scenarios.ID, Scenarios.ShortDescription FROM Scenarios WHERE (((Scenarios.HeroPos)={position}) AND ((Scenarios.VillainPos)={opponent}) AND ((Scenarios.Context)={context}));"
cursor.execute(query)  # Gets the correct scenario

for row in cursor.fetchall():
    scenario = row[0]     #Gets the text version of the Scenario E.g Open UTG, 4Bet BB vs CO
    scenario_text = row[1]# Gets the ID of the scenario E.G Open UTG is 1


query2 = f"SELECT TOP {questions} HoleCards.ShortName, HoleCards.Type, Options.LongText, ActionScores.Easiness, Scenarios.PotSize, Scenarios.HeroBetSize, Scenarios.HeroInvested, Scenarios.VillainInvested FROM (ActionScores INNER JOIN ((OptionSets INNER JOIN Options ON OptionSets.Option = Options.ID) INNER JOIN Scenarios ON OptionSets.Scenario = Scenarios.ID) ON ActionScores.[OptionSet] = OptionSets.ID) INNER JOIN HoleCards ON ActionScores.HoleCards = HoleCards.ID WHERE (((OptionSets.Scenario)={scenario}) AND ((ActionScores.Easiness) >= {difficulty}) AND ((ActionScores.Correct)=True)) ORDER BY Rnd(INT(NOW*[ActionScores]![HoleCards])-NOW*[ActionScores]![HoleCards])"
row2 = cursor.execute(query2)  # Gets cards and answers that match the type of quiz the user wants to take
