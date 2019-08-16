import sys
import csv
import numpy as np

if __name__ == '__main__':
    csv_file = open('csv/import.csv', 'r', encoding='ms932', errors=', newline=' )
    np.f = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\r\n', quotechar='"', skipinitialspace=True)

    np.csvList = []
    for row in np.f:
        np.colList = []
        for col in row:
            np.colList.append(col)
        np.csvList.append(row)

    print(np.csvList)

    f = open('csv/export.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(np.csvList)
    f.close()