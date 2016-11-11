# Count amount of "zeros" in all candidates of the exam.

import csv
import os

x = 0

print "x = " + str(x)

with open("a.csv", "rb") as source:

    rdr = csv.reader( source )

    for r in rdr:

        if r[5] != 'NUM_CN':

            soma = int(r[5]) + int(r[6]) + int(r[7]) + int(r[8])

            if soma == 0:

                os.system("cls")

                x = x + 1
                print "x = " + str(x)

            soma = 0

print("Press any key to close terminal")
input()
