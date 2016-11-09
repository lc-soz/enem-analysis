#Count correct answers in essay.

import csv

def compare(a, b): #Function for the amount of equal characters in a string

    i = 0

    for x, y in zip(a, b):

        if x == y:

            i = i + 1

    return i

with open("ENEM2014_1.csv","rb") as source:

    rdr = csv.reader( source )

    with open("a.csv","wb") as result:

        wtr = csv.writer( result )

        for r in rdr:

            if r[0] == 'NOTA_CN':

                # Header
                wtr.writerow((r[0], r[1], r[2], r[3], 'TP_LINGUA', 'NUM_CN', 'NUM_CH', 'NUM_LC', 'NUM_MT'))

            elif not(r[0] == "" and r[1] == "" and r[2] == "" and r[3] == ""): # This test if all four end-grades are not blank, if not, don't write to final file
	
                # Ciencias da Natureza
                a = compare(r[4], r[9])
				
                # Ciencias Humanas
                b = compare(r[5], r[10])
				
                # Linguagens e Codigos
                if r[11] != "":

                    lcMtx = list(r[11])

                    if r[8] == 0:

                        for z in range(0,5):
                        
                            lcMtx.pop([6])

                    else:

                        for z in range(0,5):
                        
                            lcMtx.pop(1)

                    lcGab = ''.join(lcMtx)

                    c = compare(r[6], lcGab)

                # Matematica
                d = compare(r[7], r[12])

                wtr.writerow((r[0], r[1], r[2], r[3], r[8], a, b, c, d))
                a = 0
                b = 0
                c = 0
                d = 0
                
print("Press any key to close terminal")
input()
