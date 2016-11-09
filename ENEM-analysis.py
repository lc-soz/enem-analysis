# Write min and max scores in exam from the amount of correct marks.

import csv
import os

# Variables min and max
var = [[0 for x in range(0,45)] for x in range(0,8)]

for i in (0,2,4,6):

    for z in range(0,45):

        var[i][z] = 1000

with open("C:/Users/luc-s/Desktop/a.csv", "rb") as source:

    rdr = csv.reader(source)

    with open("ENEM_analysis.csv", "wb") as result:

        wtr = csv.writer(result)

        wtr.writerow(("", "CN", "", "CH", "", "LC", "", "MT"))
        wtr.writerow(("NUM", "MIN", "MAX", "MIN", "MAX", "MIN", "MAX", "MIN", "MAX"))

        for i in range (0,46):
            
            with open("C:/Users/luc-s/Desktop/a.csv", "rb") as source:
                
                rdr = csv.reader(source)

                for r in rdr:

                    if r[0] != "NOTA_CN":

                        # Ciencias da Natureza
                        if int(r[5]) == i and r[0] != "" and float(r[0]) > 0:
                            var[0][i] = min(var[0][i], float(r[0]))
                            var[1][i] = max(var[1][i], float(r[0]))

                        # Ciencias Humanas
                        if int(r[6]) == i and r[1] != "" and float(r[1]) > 0:
                            var[2][i] = min(var[2][i], float(r[1]))
                            var[3][i] = max(var[3][i], float(r[1]))

                        # Letras e Codigos
                        if int(r[7]) == i and r[2] != "" and float(r[2]) > 0:
                            var[4][i] = min(var[4][i], float(r[2]))
                            var[5][i] = max(var[5][i], float(r[2]))

                        # Matematica
                        if int(r[8]) == i and r[3] != "" and float(r[3]) > 0:
                            var[6][i] = min(var[6][i], float(r[3]))
                            var[7][i] = max(var[7][i], float(r[3]))
            print(i)
            wtr.writerow((i, var[0][i], var[1][i], var[2][i], var[3][i], var[4][i], var[5][i], var[6][i], var[7][i]))

print("Press any key to close terminal")
input()
