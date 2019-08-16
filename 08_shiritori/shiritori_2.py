import csv
import numpy as np
from shiritori_str_convert import ConvertShiritori

from shiritori_AI_kusozakonamekuji import ShiritoriAiKusozakonamekuji
from shiritori_AI_yowai import ShiritoriAiYowai
from shiritori_AI_hutsuu import ShiritoriAiHutsuu
from shiritori_AI_bimyou import ShiritoriAiBimyou
from shiritori_AI_tsuyoi import ShiritoriAiTsuyoi
from shiritori_AI_saikyo import ShiritoriAiSaikyo
from shiritori_AI_hutsuuEx import ShiritoriAiHutsuuEx
from shiritori_AI_tsuyokunaru import ShiritoriAiTsuyokunaru
from shiritori_AI_tsuyokunaru_2 import ShiritoriAiTsuyokunaru2

def hantei(_inShiritoriAnswer,_inShiritoriAnswerBefore,_inVocList,_inShiritoriAnswerLog):
    hanteiFlg = 0
    if len(_inShiritoriAnswer)==3:
        if _inShiritoriAnswer[2][-1:] == 'ン':
            hanteiFlg = 1
            print('言葉の最後に「ん」がつきました')
        if _inShiritoriAnswerBefore[2][-1:] != _inShiritoriAnswer[2][0]:
            hanteiFlg = 1
            print('一つ前の語句の最後の文字と今の語句の最初の文字が一致しません')
        if len(_inShiritoriAnswerLog) > 1 :
            for log in _inShiritoriAnswerLog :
                if len(log) == 3:
                    if log[0] == _inShiritoriAnswer[0] and log[1] == _inShiritoriAnswer[1] and log[2] == _inShiritoriAnswer[2]:
                        hanteiFlg = 1
                        print('もう既に言われた語句です')
        sonzaiFlg = 0
        for voc in _inVocList :
            if len(voc)==3:
                if voc[0] == _inShiritoriAnswer[0] and voc[1] == _inShiritoriAnswer[1] and voc[2] == _inShiritoriAnswer[2]:
                    sonzaiFlg = 1
        if sonzaiFlg == 0:
            hanteiFlg = 1
            print('辞書に存在しない語句です')
    else :
        hanteiFlg = 1
        print('返却された語句の形式が不正です')

    return hanteiFlg

if __name__ == "__main__":

    csv_file = open("dic.csv", "r", encoding="ms932", errors="", newline="" )
    np.f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    np.vocList = [[]]
    for row in np.f:
        np.colList = []
        for col in row:
            np.colList.append(col)
        np.vocList.append(row)

    player_1_win = 0
    player_2_win = 0

    for i in range(100001):
        #player_ = ShiritoriAiSaikyo('しりとりさいきょうくん',np.vocList)
        player_1 = ShiritoriAiTsuyokunaru('しりとりつよくなるくんその壱',np.vocList)
        player_2 = ShiritoriAiTsuyokunaru2('しりとりつよくなるくんその弐',np.vocList)
        #player_1 = ShiritoriAiTsuyoi('しりとりつよいくん',np.vocList)
        #player_ = ShiritoriAiBimyou('しりとりびみょうくん',np.vocList)
        #player_1 = ShiritoriAiHutsuuEx('しりとりふつうくんEx',np.vocList)
        #player_1 = ShiritoriAiHutsuu('しりとりふつうくん',np.vocList)
        #player_ = ShiritoriAiYowai('しりとりよわいくん',np.vocList)
        #player_ = ShiritoriAiKusozakonamekuji('しりとりクソザコナメクジくん',np.vocList)

        print('スタート')

        gameoverFlg = 0
        playerNum = 1
        shiritoriAnswer = ['0','しりとり','シリトリ']
        shiritoriAnswerLog = [[]]
        shiritoriNum = 0

        while gameoverFlg == 0:
            shiritoriNum += 1
            shiritoriAnswerBefore = shiritoriAnswer

            if playerNum == 1:
                print(player_1.name +'の番です turn:'+str(shiritoriNum))
                shiritoriAnswer = player_1.shiritoriAI(shiritoriAnswerBefore)
                print(shiritoriAnswer)
            if playerNum == 2:
                print(player_2.name + 'の番です turn:'+str(shiritoriNum))
                shiritoriAnswer = player_2.shiritoriAI(shiritoriAnswerBefore)
                print(shiritoriAnswer)

            if hantei(shiritoriAnswer,shiritoriAnswerBefore,np.vocList,shiritoriAnswerLog)==0:
                if playerNum == 1:
                    playerNum = 2
                    shiritoriAnswerLog.append(shiritoriAnswer)
                else :
                    playerNum = 1
                    shiritoriAnswerLog.append(shiritoriAnswer)
            else :
                gameoverFlg = 1

        if playerNum == 1 :
            print(player_2.name +'の勝ちです')
            player_1.feedback(0)
            player_2.feedback(1)
            player_2_win += 1
        elif playerNum == 2 :
            print(player_1.name +'の勝ちです')
            player_1.feedback(1)
            player_2.feedback(0)
            player_1_win += 1

        print('-対戦成績-')
        print(player_1.name + str(player_1_win) + '勝 ' +  player_2.name + str(player_2_win) + '勝 ', flush=True)

