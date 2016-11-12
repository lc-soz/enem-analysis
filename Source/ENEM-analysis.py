# Write min and max scores in exam from the amount of correct marks.

import csv
import os
import time

t0 = time.time() # For run time (wall time)

global var

# Matrix with all cell_grades
var = [[0 for x in range(0,46)] for x in range(0,8)]

for i in (0,2,4,6):

    for z in range(0,46):

        var[i][z] = 1000

def save_values(cell_grade):

        global cell_answer

        cell_answer = 5 + cell_grade
        var_pos = cell_grade * 2

        if is_value_correct(cell_grade):
            
            value_answer = int(r[cell_answer])
            var[var_pos][value_answer] = min(var[var_pos][value_answer], float(r[cell_grade]))
            var[(var_pos + 1)][value_answer] = max(var[(var_pos + 1)][value_answer], float(r[cell_grade]))
            
def is_value_correct(cell_grade):
        
        if r[cell_answer] != "" and r[cell_grade] != "" and float(r[cell_grade]) > 0:
        
            return True
            
with open("C:/Users/luc-s/Desktop/a.csv", "rb") as source:

    rdr = csv.reader(source)

    with open("ENEM-analysis.csv", "wb") as result:

        wtr = csv.writer(result)

        # HEADER
        wtr.writerow(("", "CN", "", "CH", "", "LC", "", "MT"))
        wtr.writerow(("NUM", "MIN", "MAX", "MIN", "MAX", "MIN", "MAX", "MIN", "MAX"))

        with open("C:/Users/luc-s/Desktop/a.csv", "rb") as source:

            next(rdr, None)
            
            for r in rdr:
                
                # Ciencias da Natureza 
                save_values(0)

                # Ciencias Humanas 
                save_values(1)

                # Letras e Codigos 
                save_values(2)

                # Matematica 
                save_values(3)

            for z in range(0, 46):
                
                wtr.writerow((z, var[0][z], var[1][z], var[2][z], var[3][z], var[4][z], var[5][z], var[6][z], var[7][z]))

print str(time.time() - t0)
print("Press any key")
input()
