# Simple progress function

import time
import os

for x in range (1, 11):

    a = (float(x) / 10) * 100

    print (str(a) + "%")

    time.sleep(0.3)

    os.system("cls")

print (str(a) + "%")

input("Press anything to close")
