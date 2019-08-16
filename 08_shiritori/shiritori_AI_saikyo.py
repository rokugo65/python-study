import numpy as np
import random

class ShiritoriAiSaikyo:

    def __init__(self,_inName,_inVocList):
        self.name = _inName
        self.vocList = _inVocList
        self.vocSortList = [[]]
        self.vocAnswerLogList = [[]]
        self.mojizemeList = ['ズ','ペ','ピ','ゾ','ル','グ','プ','ボ','ポ','モ','ガ','ヘ','サ','ゼ','ハ','ゲ','ス','ゴ','ザ','オ','ホ','ベ','バ','ラ','ク','ブ','ヤ','ダ','ジ','ツ','ニ','チ','レ','ギ','エ','ノ','ヌ','シ','ヨ','ミ','パ','タ','ワ','ア','ケ','ム','イ','セ','ナ','ウ','メ','コ','カ','ド','ビ','リ','マ','ヒ','ネ','キ','フ','テ','ト','ユ','ソ','ロ','デ']

        for moji in self.mojizemeList :
            for voc in self.vocList :
                if len(voc) == 3:
                    if voc[2][-1:] == moji:
                        self.vocSortList.append(voc)

    def shiritoriAI(self, _inShiritoriAnswer):
        self.vocAnswerLogList.append(_inShiritoriAnswer)
        if len(_inShiritoriAnswer) == 3 and len(self.vocList) > 0:
            for voc in self.vocSortList:
                if len(voc) == 3 :
                    if voc[2][0] == _inShiritoriAnswer[2][-1:] and voc[2][-1:]!='ン':
                        sonzaiFlg = 0
                        for log in self.vocAnswerLogList :
                            if len(log) == 3 :
                                if log[0] == voc[0] and log[1] == voc[1] and log[2] == voc[2]:
                                    sonzaiFlg = 1
                                    break
                        if sonzaiFlg == 0 :
                            _inShiritoriAnswer = voc
                            break

        self.vocAnswerLogList.append(_inShiritoriAnswer)
        return _inShiritoriAnswer

    def feedback(self, _inResult):
        if _inResult==1:
            hoge = 1