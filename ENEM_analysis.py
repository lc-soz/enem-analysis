#Write min and max scores in essay from the amount of right marks.

import csv
import os

#Variables min and max
global minCN
global maxCN
global minCH
global maxCH
global minLC
global maxLC
global minMT
global maxMT

with open("a.csv", "rb") as source:

    rdr = csv.reader(source)

    with open("ENEM_analysis.csv", "wb") as result:

        wtr = csv.writer(result)

        wtr.writerow(("", "CN", "", "CH", "", "LC", "", "MT"))
        wtr.writerow(("NUM", "MIN", "MAX", "MIN", "MAX", "MIN", "MAX", "MIN", "MAX"))

        for i in range (0,46):
            
            #Variables min and max
            minCN = 1000
            maxCN = 0
            minCH = 1000
            maxCH = 0
            minLC = 1000
            maxLC = 0
            minMT = 1000
            maxMT = 0
            with open("a.csv", "rb") as source:
                
                rdr = csv.reader(source)

                for r in rdr:

                    if r[0] != "NOTA_CN":

                        #Ciencias da Natureza
                        if int(r[5]) == i and r[0] != "" and float(r[0]) > 0:
                            minCN = min(minCN, float(r[0]))
                            maxCN = max(maxCN, float(r[0]))

                        #Ciencias Humanas
                        if int(r[6]) == i and r[1] != "" and float(r[1]) > 0:
                            minCH = min(minCH, float(r[1]))
                            maxCH = max(maxCH, float(r[1]))

                        #Letras e Codigos
                        if int(r[7]) == i and r[2] != "" and float(r[2]) > 0:
                            minLC = min(minLC, float(r[2]))
                            maxLC = max(maxLC, float(r[2]))

                        #Matematica
                        if int(r[8]) == i and r[3] != "" and float(r[3]) > 0:
                            minMT = min(minMT, float(r[3]))
                            maxMT = max(maxMT, float(r[3]))
            print(i)
            wtr.writerow((i, minCN, maxCN, minCH, maxCH, minLC, maxLC, minMT, maxMT))

print("Press any key to close terminal")
input()
