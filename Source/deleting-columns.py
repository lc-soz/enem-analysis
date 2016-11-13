# Deleting not useful columns from file.

import csv
import time

t0 = time.time() # For run time (wall time)

def none_null_score():
    
    test = False
    scores = [r[y] for y in range(70,74)]
    
    for z in scores:
    
        if z != "":
            
            test = True
    
    return test

with open("C:\TESTS\MICRODADOS_ENEM_2014.csv","rb") as source:

    rdr = csv.reader( source )

    with open("C:\TESTS\ENEM2014.csv","wb") as result:

        wtr = csv.writer( result )

        for r in rdr:
        
            if none_null_score():
                
                row = [r[x] for x in range(70,83)]
                wtr.writerow(row)

print "deleting-columns: " + str(time.time() - t0)
