import csv
import re
import numpy as np
import random
from tqdm import tqdm
from shiritori_str_convert import ConvertShiritori
from shiritori_AI_hutsuu import ShiritoriAiHutsuu

def hantei(_inShiritoriAnswer,_inShiritoriAnswerBefore,_inVocList,_inShiritoriAnswerLog):
    hanteiFlg = 0
    if len(_inShiritoriAnswer)==3:
        if _inShiritoriAnswer[2][-1:] == 'ン':
            hanteiFlg = 1
            #print('言葉の最後に「ん」がつきました')
        if _inShiritoriAnswerBefore[2][-1:] != _inShiritoriAnswer[2][0]:
            hanteiFlg = 1
            #print('一つ前の語句の最後の文字と今の語句の最初の文字が一致しません')
        if len(_inShiritoriAnswerLog) > 1 :
            for log in _inShiritoriAnswerLog :
                if len(log) == 3:
                    if log[0] == _inShiritoriAnswer[0] and log[1] == _inShiritoriAnswer[1] and log[2] == _inShiritoriAnswer[2]:
                        hanteiFlg = 1
                        #print('もう既に言われた語句です')
        sonzaiFlg = 0
        for voc in _inVocList :
            if len(voc)==3:
                if voc[0] == _inShiritoriAnswer[0] and voc[1] == _inShiritoriAnswer[1] and voc[2] == _inShiritoriAnswer[2]:
                    sonzaiFlg = 1
        if sonzaiFlg == 0:
            hanteiFlg = 1
            #print('辞書に存在しない語句です')
    else :
        hanteiFlg = 1
        #print('返却された語句の形式が不正です')

    return hanteiFlg

csv_file = open("dic.csv", "r", encoding="ms932", errors="", newline="" )
np.f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

np.vocList = [[]]
for row in np.f:
    np.colList = []
    for col in row:
        np.colList.append(col)
    np.vocList.append(row)

AI_1 = ShiritoriAiHutsuu()

hiraganaSyouritsu = [
    ['ア',1,1,50], ['イ',1,1,50], ['ウ',1,1,50], ['エ',1,1,50], ['オ',1,1,50],
    ['カ',1,1,50], ['キ',1,1,50], ['ク',1,1,50], ['ケ',1,1,50], ['コ',1,1,50],
    ['サ',1,1,50], ['シ',1,1,50], ['ス',1,1,50], ['セ',1,1,50], ['ソ',1,1,50],
    ['タ',1,1,50], ['チ',1,1,50], ['ツ',1,1,50], ['テ',1,1,50], ['ト',1,1,50],
    ['ナ',1,1,50], ['ニ',1,1,50], ['ヌ',1,1,50], ['ネ',1,1,50], ['ノ',1,1,50],
    ['ハ',1,1,50], ['ヒ',1,1,50], ['フ',1,1,50], ['ヘ',1,1,50], ['ホ',1,1,50],
    ['マ',1,1,50], ['ミ',1,1,50], ['ム',1,1,50], ['メ',1,1,50], ['モ',1,1,50],
    ['ヤ',1,1,50], ['ユ',1,1,50], ['ヨ',1,1,50],
    ['ラ',1,1,50], ['リ',1,1,50], ['ル',1,1,50], ['レ',1,1,50], ['ロ',1,1,50],
    ['ワ',1,1,50], ['ヲ',1,1,50], ['ン',1,1,50],
    ['ガ',1,1,50], ['ギ',1,1,50], ['グ',1,1,50], ['ゲ',1,1,50], ['ゴ',1,1,50],
    ['ザ',1,1,50], ['ジ',1,1,50], ['ズ',1,1,50], ['ゼ',1,1,50], ['ゾ',1,1,50],
    ['ダ',1,1,50], ['ヂ',1,1,50], ['ヅ',1,1,50], ['デ',1,1,50], ['ド',1,1,50],
    ['バ',1,1,50], ['ビ',1,1,50], ['ブ',1,1,50], ['ベ',1,1,50], ['ボ',1,1,50],
    ['パ',1,1,50], ['ピ',1,1,50], ['プ',1,1,50], ['ペ',1,1,50], ['ポ',1,1,50]
]

kachi_1 = 0
kachi_2 = 0
tqdm.monitor_interval =  0
pbar = tqdm(total=2000)

for j in range(2000):
    pbar.update(1)
    #print('')
    #print(str(j+1)+'回目')
    #print('player1:'+str(kachi_1)+' player2:'+str(kachi_2))
    hiraganaPlayer1 = [
        ['ア',0], ['イ',0], ['ウ',0], ['エ',0], ['オ',0],
        ['カ',0], ['キ',0], ['ク',0], ['ケ',0], ['コ',0],
        ['サ',0], ['シ',0], ['ス',0], ['セ',0], ['ソ',0],
        ['タ',0], ['チ',0], ['ツ',0], ['テ',0], ['ト',0],
        ['ナ',0], ['ニ',0], ['ヌ',0], ['ネ',0], ['ノ',0],
        ['ハ',0], ['ヒ',0], ['フ',0], ['ヘ',0], ['ホ',0],
        ['マ',0], ['ミ',0], ['ム',0], ['メ',0], ['モ',0],
        ['ヤ',0], ['ユ',0], ['ヨ',0],
        ['ラ',0], ['リ',0], ['ル',0], ['レ',0], ['ロ',0],
        ['ワ',0], ['ヲ',0], ['ン',0],
        ['ガ',0], ['ギ',0], ['グ',0], ['ゲ',0], ['ゴ',0],
        ['ザ',0], ['ジ',0], ['ズ',0], ['ゼ',0], ['ゾ',0],
        ['ダ',0], ['ヂ',0], ['ヅ',0], ['デ',0], ['ド',0],
        ['バ',0], ['ビ',0], ['ブ',0], ['ベ',0], ['ボ',0],
        ['パ',0], ['ピ',0], ['プ',0], ['ペ',0], ['ポ',0]
    ]

    hiraganaPlayer2 = [
        ['ア',0], ['イ',0], ['ウ',0], ['エ',0], ['オ',0],
        ['カ',0], ['キ',0], ['ク',0], ['ケ',0], ['コ',0],
        ['サ',0], ['シ',0], ['ス',0], ['セ',0], ['ソ',0],
        ['タ',0], ['チ',0], ['ツ',0], ['テ',0], ['ト',0],
        ['ナ',0], ['ニ',0], ['ヌ',0], ['ネ',0], ['ノ',0],
        ['ハ',0], ['ヒ',0], ['フ',0], ['ヘ',0], ['ホ',0],
        ['マ',0], ['ミ',0], ['ム',0], ['メ',0], ['モ',0],
        ['ヤ',0], ['ユ',0], ['ヨ',0],
        ['ラ',0], ['リ',0], ['ル',0], ['レ',0], ['ロ',0],
        ['ワ',0], ['ヲ',0], ['ン',0],
        ['ガ',0], ['ギ',0], ['グ',0], ['ゲ',0], ['ゴ',0],
        ['ザ',0], ['ジ',0], ['ズ',0], ['ゼ',0], ['ゾ',0],
        ['ダ',0], ['ヂ',0], ['ヅ',0], ['デ',0], ['ド',0],
        ['バ',0], ['ビ',0], ['ブ',0], ['ベ',0], ['ボ',0],
        ['パ',0], ['ピ',0], ['プ',0], ['ペ',0], ['ポ',0]
    ]

    #print('スタート')

    gameoverFlg = 0
    playerNum = 1
    shiritoriAnswer = ['0','しりとり','シリトリ']
    shiritoriAnswerLog = [[]]
    shiritoriNum = 0

    while gameoverFlg == 0:
        shiritoriNum += 1
        shiritoriAnswerBefore = shiritoriAnswer

        if playerNum == 1:
            #print('player1の番です turn:'+str(shiritoriNum))
            shiritoriAnswer = AI_1.shiritoriAI(np.vocList,shiritoriAnswerBefore,shiritoriAnswerLog)
            #print(shiritoriAnswer)
            if len(shiritoriAnswer)==3:
                for hiragana in hiraganaPlayer1:
                    if len(hiragana) == 2:
                        if hiragana[0] == shiritoriAnswer[2][-1:]:
                            hiragana[1] += 1
        if playerNum == 2:
            #print('player2の番です turn:'+str(shiritoriNum))
            shiritoriAnswer = AI_1.shiritoriAI(np.vocList,shiritoriAnswerBefore,shiritoriAnswerLog)
            #print(shiritoriAnswer)
            if len(shiritoriAnswer)==3:
                for hiragana in hiraganaPlayer2:
                    if len(hiragana) == 2:
                        if hiragana[0] == shiritoriAnswer[2][-1:]:
                            hiragana[1] += 1

        if hantei(shiritoriAnswer,shiritoriAnswerBefore,np.vocList,shiritoriAnswerLog)==0:
            if playerNum == 1:
                playerNum = 2
                shiritoriAnswerLog.append(shiritoriAnswer)
            else :
                playerNum = 1
                shiritoriAnswerLog.append(shiritoriAnswer)
        else :
            gameoverFlg = 1

    #print(str(playerNum)+'の負けです')
    if playerNum == 1:
        kachi_2 += 1
        if len(shiritoriAnswer)==3:
            for hiragana in hiraganaPlayer1:
                if len(hiragana) == 2:
                    if hiragana[0] == shiritoriAnswer[2][-1:]:
                        hiragana[1] -= 1
        for i in range(71):
            if len(hiraganaSyouritsu)==71 and len(hiraganaPlayer1)==71 and len(hiraganaPlayer2)==71:
                if len(hiraganaSyouritsu[i])==4 and len(hiraganaPlayer1[i])==2 and len(hiraganaPlayer2[i])==2:
                    hiraganaSyouritsu[i][1] += hiraganaPlayer2[i][1]
                    hiraganaSyouritsu[i][2] += hiraganaPlayer1[i][1]
    else :
        kachi_1 += 1
        if len(shiritoriAnswer)==3:
            for hiragana in hiraganaPlayer2:
                if len(hiragana) == 2:
                    if hiragana[0] == shiritoriAnswer[2][-1:]:
                        hiragana[1] -= 1
        for i in range(71):
            if len(hiraganaSyouritsu)==71 and len(hiraganaPlayer1)==71 and len(hiraganaPlayer2)==71:
                if len(hiraganaSyouritsu[i])==4 and len(hiraganaPlayer1[i])==2 and len(hiraganaPlayer2[i])==2:
                    hiraganaSyouritsu[i][1] += hiraganaPlayer1[i][1]
                    hiraganaSyouritsu[i][2] += hiraganaPlayer2[i][1]

print("最終成績")
print("player1:"+str(kachi_1)+" player2:"+str(kachi_2))
f = open('export.csv', 'w')
pbar.close()

writer = csv.writer(f, lineterminator='\n')
writer.writerows(hiraganaSyouritsu)

f.close()