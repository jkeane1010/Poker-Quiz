from getting_easiness import easiness_ratings_array
from getting_options import number_of_answers
from configuration import questions

scores_array = [['' for i in range (number_of_answers)] for j in range(questions)]

i = 0
while i < questions:
    z = 0
    while z < number_of_answers:
        scores_array[i][z] = ((10 - easiness_ratings_array[i][z])*10)
        z += 1
    i += 1

#print(scores_array)