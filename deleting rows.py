import csv
import os

# First: Delete from NU_INSCRICAO [0] to ID_PROVA_MT [69]
with open("F:\Microdados ENEM\microdados_enem2014\DADOS\MICRODADOS_ENEM_2014.csv","rb") as source:

    rdr = csv.reader( source )

    with open("ENEM2014.csv","wb") as result:

        wtr = csv.writer( result )

        for r in rdr:

            for x in range( 0,70 ):

                del r[0]

            wtr.writerow( r )

# Second: Delete from IN_STATUS_REDACAO [83] to Q076 [165]
# After First: [13] to [95]
with open("ENEM2014.csv","rb") as source:

    rdr = csv.reader( source )

    with open("ENEM2014_1.csv","wb") as result:

        wtr = csv.writer( result )

        for r in rdr:

            for x in range( 13,96 ):

                del r[13]

            wtr.writerow( r )

print("Press any key to close terminal")
input()
