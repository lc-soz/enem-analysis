# Count correct answers in exam.

import csv
import time

t0 = time.time() # For run time (wall time)

def compare(a, b): #Function for the amount of equal characters in a string
    
    cell_score = a - 4
    
    if r[cell_score] != "": 
        
        i = 0

        for x, y in zip(r[a], b):

            if x == y:

                i = i + 1

        return i
        
    else:
        
        return ""

with open("C:\TESTS\ENEM2014.csv","rb") as source:

    rdr = csv.reader( source )

    with open("C:\TESTS\end.csv","wb") as result:

        wtr = csv.writer( result )
        
        wtr.writerow(('NOTA_CN', 'NOTA_CH', 'NOTA_LC', 'NOTA_MT', 'TP_LINGUA', 'NUM_CN', 'NUM_CH', 'NUM_LC', 'NUM_MT')) #HEADER

        next(rdr, None)
        for r in rdr:

            ciencias_da_natureza = compare(4, r[9])
            
            ciencias_humanas = compare(5, r[10])

            if r[11] != "":

                matrix_ligcod = list(r[11])

                if r[8] == 0:

                    for z in range(0, 5):
                    
                        matrix_ligcod.pop([6])

                else:

                    for z in range(0, 5):
                    
                        matrix_ligcod.pop(1)

                gabarito_ligcod = ''.join(matrix_ligcod)

                linguagens_e_codigos = compare(6, gabarito_ligcod)

            matematica = compare(7, r[12])

            wtr.writerow((r[0], r[1], r[2], r[3], r[8], ciencias_da_natureza, ciencias_humanas, linguagens_e_codigos, matematica))
            ciencias_da_natureza = ""
            ciencias_humanas = ""
            linguagens_e_codigos = ""
            matematica = ""

print str(time.time() - t0)                
print("Press any key to close terminal")
input()
