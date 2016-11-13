# Run all parts of the program at order

import os
import time

t0 = time.time() # For run time (wall time)

os.system("deleting-columns.py")
os.system("count-corrects.py")
os.system("ENEM-analysis.py")

print "run: " + str(time.time() - t0)