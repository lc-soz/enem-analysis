# Deleting not useful columns from file

import csv
import time

t0 = time.time() # For run time (wall time)

# First: Delete from NU_INSCRICAO [0] to ID_PROVA_MT [69]
with open("C:\TESTS\MICRODADOS_ENEM_2014.csv","rb") as source:

    rdr = csv.reader( source )

    with open("C:\TESTS\ENEM2014.csv","wb") as result:

        wtr = csv.writer( result )

        for r in rdr:

            row = [r[x] for x in range(70,83)]
            wtr.writerow(row)

print str(time.time() - t0)
print("Press any key")
input()
