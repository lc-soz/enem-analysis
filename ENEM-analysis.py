# Write min and max scores in exam from the amount of correct marks.

import csv
import os

# Variables min and max
global var
var = [[0 for x in range(0,46)] for x in range(0,8)]

for i in (0,2,4,6):

    for z in range(0,46):

        var[i][z] = 1000

with open("C:/Users/luc-s/Desktop/a.csv", "rb") as source:

    rdr = csv.reader(source)

    with open("ENEM_analysis.csv", "wb") as result:

        wtr = csv.writer(result)

        wtr.writerow(("", "CN", "", "CH", "", "LC", "", "MT"))
        wtr.writerow(("NUM", "MIN", "MAX", "MIN", "MAX", "MIN", "MAX", "MIN", "MAX"))

        with open("C:/Users/luc-s/Desktop/a.csv", "rb") as source:

            rdr = csv.reader(source)

            for r in rdr:

                if r[0] != "NOTA_CN":

                    # Ciencias da Natureza
                    if r[5] != "" and r[0] != "" and float(r[0]) > 0:

                        i = int(r[5])
                        var[0][i] = min(var[0][i], float(r[0]))
                        var[1][i] = max(var[1][i], float(r[0]))

                    # Ciencias Humanas
                    if r[6] != "" and r[1] != "" and float(r[1]) > 0:

                        i = int(r[6])
                        var[2][i] = min(var[2][i], float(r[1]))
                        var[3][i] = max(var[3][i], float(r[1]))

                    # Letras e Codigos
                    if r[7] != "" and r[2] != "" and float(r[2]) > 0:

                        i = int(r[7])
                        var[4][i] = min(var[4][i], float(r[2]))
                        var[5][i] = max(var[5][i], float(r[2]))

                    # Matematica
                    if r[8] != "" and r[3] != "" and float(r[3]) > 0:

                        i = int(r[8])
                        var[6][i] = min(var[6][i], float(r[3]))
                        var[7][i] = max(var[7][i], float(r[3]))

                    #if int(r[5]) == 45:

                        #print r[0]

            for z in range(0, 46):
     
                wtr.writerow((z, var[0][z], var[1][z], var[2][z], var[3][z], var[4][z], var[5][z], var[6][z], var[7][z]))

print("Press any key to close terminal")
input()
