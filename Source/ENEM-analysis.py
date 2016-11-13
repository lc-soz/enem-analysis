# Write min and max scores in exam from the amount of correct marks.

import csv
import time

t0 = time.time() # For run time (wall time)

var = [[0 for x in range(0,46)] for x in range(0,8)] # Matrix with min and max scores

for i in (0,2,4,6):

    for z in range(0,46):

        var[i][z] = 1000

# Functions
def save_values(cell_grade, cell_answer):

        var_pos = cell_grade * 2
        var_pos_plus = var_pos + 1

        if is_value_correct(cell_grade, cell_answer):
            
            value_answer = int(r[cell_answer])
            var[var_pos][value_answer] = min(var[var_pos][value_answer], float(r[cell_grade]))
            var[var_pos_plus][value_answer] = max(var[var_pos_plus][value_answer], float(r[cell_grade]))
            
# Methods
def is_value_correct(cell_grade, cell_answer):
        
        if r[cell_answer] != "" and r[cell_grade] != "" and float(r[cell_grade]) > 0:
        
            return True
            
with open("C:\TESTS\end.csv", "rb") as source:

    rdr = csv.reader(source)

    with open("C:\TESTS\ENEM-analysis.csv", "wb") as result:

        wtr = csv.writer(result)

        # HEADER
        wtr.writerow(["", "CN", "", "CH", "", "LC", "", "MT"])
        wtr.writerow(["NUM"] + ["MIN", "MAX"] * 4)

        next(rdr, None)
        
        for r in rdr:
            
            # Ciencias da Natureza 
            save_values(0, 5)

            # Ciencias Humanas 
            save_values(1, 6)

            # Letras e Codigos 
            save_values(2, 7)

            # Matematica 
            save_values(3, 8)

        for z in range(0, 46):
            
            row = ([z] + [var[x][z] for x in range(0,8)])
            wtr.writerow(row)

print "ENEM-analysis: " + str(time.time() - t0)