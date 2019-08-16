import sys
import csv
import numpy as np

def lifestyleCheckLogic(_inNum1,_inNum2,_inNum3,_inNum4,_inNum5,_inNum6):
    #_outLifestyleType = 'none'
    _outLifestyleType = '特定不可'
    if _inNum3 > _inNum1 and _inNum3 > _inNum2 and _inNum3 > _inNum5 and _inNum3 > _inNum6 and _inNum4 > _inNum1 and _inNum4 > _inNum2 and _inNum4 > _inNum5 and _inNum4 > _inNum6 and abs(_inNum3 - _inNum4) <= 2 :
        # ドライバーとコントローラーが他のすべての値より大きいかつドライバーとコントローラーの差が2以下
        #_outLifestyleType = 'kanpekisyugi'
        _outLifestyleType = '完璧主義'
    elif _inNum1 > _inNum2 and _inNum1 > _inNum4 and _inNum1 > _inNum5 and _inNum1 > _inNum6 and _inNum3 > _inNum2 and _inNum3 > _inNum4 and _inNum3 > _inNum5 and _inNum3 > _inNum6 and abs(_inNum1 - _inNum3) <= 2 :
        # ゲッターとドライバーが他のすべての値より大きいかつゲッターとドライバーの差が2以下
        #_outLifestyleType = 'yarite'
        _outLifestyleType = 'やり手'
    elif _inNum2 > _inNum1 and _inNum2 > _inNum4 and _inNum2 > _inNum5 and _inNum2 > _inNum6 and _inNum3 > _inNum1 and _inNum3 > _inNum4 and _inNum3 > _inNum5 and _inNum3 > _inNum6 and abs(_inNum2 - _inNum3) <= 2 :
        # ベイビーとドライバーが他のすべての値より大きいかつベイビーとドライバーの差が2以下
        #_outLifestyleType = 'yorokobaseya'
        _outLifestyleType = '喜ばせ屋'
    elif _inNum1 > _inNum2 and _inNum1 > _inNum3 and _inNum1 > _inNum4 and _inNum1 > _inNum5 and _inNum1 > _inNum6 :
        # ゲッターが他のすべての値より大きい
        #_outLifestyleType = 'yokubari'
        _outLifestyleType = '欲張り'
    elif _inNum2 > _inNum1 and _inNum2 > _inNum3 and _inNum2 > _inNum4 and _inNum2 > _inNum5 and _inNum2 > _inNum6 :
        # ベイビーが他のすべての値より大きい
        #_outLifestyleType = 'akanbou'
        _outLifestyleType = '赤ん坊'
    elif _inNum3 > _inNum1 and _inNum3 > _inNum2 and _inNum3 > _inNum4 and _inNum3 > _inNum5 and _inNum3 > _inNum6 :
        # ドライバーが他のすべての値より大きい
        #_outLifestyleType = 'ningenkikansya'
        _outLifestyleType = '人間機関車'
    elif _inNum4 > _inNum1 and _inNum4 > _inNum2 and _inNum4 > _inNum3 and _inNum4 > _inNum5 and _inNum4 > _inNum6 :
        # コントローラーが他のすべての値より大きい
        #_outLifestyleType = 'jikoyokusei'
        _outLifestyleType = '自己抑制'
    elif _inNum5 > _inNum1 and _inNum5 > _inNum2 and _inNum5 > _inNum3 and _inNum5 > _inNum4 and _inNum5 > _inNum6 :
        # エクサイトメントシーカーが他のすべての値より大きい
        _outLifestyleType = '興奮探し'
    elif _inNum6 > _inNum1 and _inNum6 > _inNum2 and _inNum6 > _inNum3 and _inNum6 > _inNum4 and _inNum6 > _inNum5 :
        # アームチェアーが他のすべての値より大きい
        _outLifestyleType = '安楽'
    else :
        # どれにも属さない
        _outLifestyleType = '特定不可'
        
    return _outLifestyleType


if __name__ == '__main__':
    csv_file = open('csv/import.txt', 'r', encoding='ms932', errors=', newline=' )
    np.f = csv.reader(csv_file, delimiter='\t', doublequote=True, lineterminator='\r\n', quotechar='"', skipinitialspace=True)

    np.csvList = []
    for row in np.f:
        np.colList = []
        for col in row:
            np.colList.append(col)
        np.csvList.append(row)

    np.csvList[0].append('getter')
    np.csvList[0].append('baby')
    np.csvList[0].append('driver')
    np.csvList[0].append('controller')
    np.csvList[0].append('excitement_seeker')
    np.csvList[0].append('arm_chair')
    np.csvList[0].append('lifestyley_type')
    #print(np.csvList)
    for i in range(1,len(np.csvList)):
        print(np.csvList[i])
        num1 = int(np.csvList[i][4]) + int(np.csvList[i][10]) + int(np.csvList[i][16]) + int(np.csvList[i][22]) + int(np.csvList[i][28]) 
        num2 = int(np.csvList[i][5]) + int(np.csvList[i][11]) + int(np.csvList[i][17]) + int(np.csvList[i][23]) + int(np.csvList[i][29]) 
        num3 = int(np.csvList[i][6]) + int(np.csvList[i][12]) + int(np.csvList[i][18]) + int(np.csvList[i][24]) + int(np.csvList[i][30]) 
        num4 = int(np.csvList[i][7]) + int(np.csvList[i][13]) + int(np.csvList[i][19]) + int(np.csvList[i][25]) + int(np.csvList[i][31]) 
        num5 = int(np.csvList[i][8]) + int(np.csvList[i][14]) + int(np.csvList[i][20]) + int(np.csvList[i][26]) + int(np.csvList[i][32]) 
        num6 = int(np.csvList[i][9]) + int(np.csvList[i][15]) + int(np.csvList[i][21]) + int(np.csvList[i][27]) + int(np.csvList[i][33]) 
        lifestyleType = lifestyleCheckLogic(num1,num2,num3,num4,num5,num6)
        np.csvList[i].append(num1)
        np.csvList[i].append(num2)
        np.csvList[i].append(num3)
        np.csvList[i].append(num4)
        np.csvList[i].append(num5)
        np.csvList[i].append(num6)
        np.csvList[i].append(lifestyleType)
        print(lifestyleType)

    f = open('csv/export.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(np.csvList)
    f.close()