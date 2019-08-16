import csv
import numpy as np
from shiritori_str_convert import ConvertShiritori

from shiritori_AI_kusozakonamekuji import ShiritoriAiKusozakonamekuji
from shiritori_AI_yowai import ShiritoriAiYowai
from shiritori_AI_hutsuu import ShiritoriAiHutsuu
from shiritori_AI_bimyou import ShiritoriAiBimyou
from shiritori_AI_tsuyoi import ShiritoriAiTsuyoi
from shiritori_AI_saikyo import ShiritoriAiSaikyo

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

def kensaku(_inStr,_inVocList,_inAnswerBefore):
    shiritoriAnswer = []
    mitukattaFlg = 0
    for voc in _inVocList:
        if len(voc) == 3 and len(_inAnswerBefore) == 3:
            if _inStr == voc[1] and voc[2][0] == _inAnswerBefore[2][-1:]:
                shiritoriAnswer = voc
                mitukattaFlg = 1
    if mitukattaFlg == 0:
        print('入力された語句は存在しません')
        shiritoriAnswer = [-1]
    
    return shiritoriAnswer

if __name__ == "__main__":

    csv_file = open("dic.csv", "r", encoding="ms932", errors="", newline="" )
    np.f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    np.vocList = [[]]
    for row in np.f:
        np.colList = []
        for col in row:
            np.colList.append(col)
        np.vocList.append(row)

    player_com = ShiritoriAiKusozakonamekuji('しりとりクソザコナメクジくん',np.vocList)

    player_win = 0
    player_com_win = 0

    print('たのしいしりとりバトル')
    print('対戦相手のつよさをえらんでね')
    print('1:さいきょう')
    print('2:つよい')
    print('3:ふつう')
    print('4:よわい')
    print('5:クソザコナメクジ')

    taisenaiteFlg = 0
    while taisenaiteFlg == 0 :
        taisenaite_str = input()
        if taisenaite_str == '1' or taisenaite_str == '１':
            player_com = ShiritoriAiSaikyo('しりとりさいきょうくん',np.vocList)
            taisenaiteFlg = 1
        elif taisenaite_str == '2' or taisenaite_str == '２':
            player_com = ShiritoriAiTsuyoi('しりとりつよいくん',np.vocList)
            taisenaiteFlg = 1
        elif taisenaite_str == '3' or taisenaite_str == '３':
            player_com = ShiritoriAiHutsuu('しりとりふつうくん',np.vocList)
            taisenaiteFlg = 1
        elif taisenaite_str == '4' or taisenaite_str == '４':
            player_com = ShiritoriAiYowai('しりとりよわいくん',np.vocList)
            taisenaiteFlg = 1
        elif taisenaite_str == '5' or taisenaite_str == '５':
            taisenaiteFlg = 1
        else :
            print('もう一度入力してください')

    print('対戦相手:'+player_com.name)

    for i in range(1):

        print('まずはしりとりの「リ」から')
        gameoverFlg = 0
        playerNum = 1
        shiritoriAnswer = ['0','しりとり','シリトリ']
        shiritoriAnswerLog = [[]]
        shiritoriNum = 0

        while gameoverFlg == 0:
            shiritoriNum += 1
            shiritoriAnswerBefore = shiritoriAnswer

            if playerNum == 1:
                print('あなたの番です turn:'+str(shiritoriNum))
                mitukattaFlg = 0
                while mitukattaFlg == 0 :
                    input_str = input()
                    shiritoriAnswer = kensaku(input_str,np.vocList,shiritoriAnswerBefore)
                    if len(shiritoriAnswer) == 3 :
                        mitukattaFlg = 1
                    else :
                        print('もう一度入力してください')
                    
                print(shiritoriAnswer)
            if playerNum == 2:
                print(player_com.name + 'の番です turn:'+str(shiritoriNum))
                shiritoriAnswer = player_com.shiritoriAI(shiritoriAnswerBefore)
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
            print(player_com.name +'の勝ちです')
            player_com_win += 1
        elif playerNum == 2 :
            print('あなたの勝ちです')
            player_win += 1

        #print('-対戦成績-')
        #print('あなた' + str(player_win) + '勝 ' +  player_com.name + str(player_com_win) + '勝 ', flush=True)

