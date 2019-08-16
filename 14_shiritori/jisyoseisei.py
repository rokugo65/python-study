import csv
import re
import numpy as np
import random
from shiritori_str_convert import ConvertShiritori

csv_file = open("dic_.csv", "r", encoding="ms932", errors="", newline="" )
np.f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

np.vocList = [[]]
for row in np.f:
    np.colList = []
    for col in row:
        np.colList.append(col)
    np.vocList.append(row)

'''
print(np.vocList)
'''

convShiri = ConvertShiritori()
for row in np.vocList:
    if len(row)>2:
        row[2] = convShiri.convertShiritori(row[2])

f = open('export.csv', 'w')

writer = csv.writer(f, lineterminator='\n')
writer.writerows(np.vocList)

f.close()

