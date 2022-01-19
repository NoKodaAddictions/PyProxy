import sys
import os

with open("{{ PATH TO routeTo.txt }}") as r:
    reader = r.read()
    
print(f"CnR is routing .py file to: {reader}..")

os.system(f"py {{ PATH TO PYPROXY FOLDER }}{reader} {sys.argv[1]}")