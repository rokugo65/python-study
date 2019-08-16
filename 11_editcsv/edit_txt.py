import sys
import csv
import numpy as np

if __name__ == '__main__':
    file = open('csv/import.txt',encoding='utf-8')
    stringList = file.readlines()
    
    longString = ''
    for string in stringList:
        string = string.replace(u'\u273f', u'')
        string = string.replace(u'\ua4b3', u'')
        string = string.replace(u'\u203c', u'')
        string = string.replace(u'\ufe0e', u'')
        string = string.replace(u'\u2665', u'')
        string = string.replace(u'\U0001f924', u'')
        string = string.replace(u'\u2661', u'')
        string = string.replace(u'\n', u'')
        string = string.replace(u'\t', u'')
        string = string.replace(u'}', u'')
        string = string.replace(u'""', u'"')
        longString += string

    np.csvList = []
    diaryList = longString.split(']')
    for diary in diaryList:
        diarySplit = diary.split('"{')
        diarySplitSplit = diarySplit[0].split('"')
        if len(diarySplitSplit) > 2:
            print(diarySplitSplit[2:])
            np.csvList.append(diarySplitSplit[2:])

    f = open('csv/export.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(np.csvList)
    f.close()

