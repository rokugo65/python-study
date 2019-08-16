import numpy as np
import random

class ShiritoriAiKusozakonamekuji:

    def __init__(self,_inName,_inVocList):
        self.name = _inName
        self.vocList = _inVocList
        self.vocAnswerLogList = [[]]
        self.mojizemeList = ['ン']

    def shiritoriAI(self, _inShiritoriAnswer):
        self.vocAnswerLogList.append(_inShiritoriAnswer)
        if len(_inShiritoriAnswer) == 3 and len(self.vocList) > 0:
            iterNum = 0
            mitukattaFlg = 0
            vocAnswerKouhoList = [[]]
            while iterNum < 100000 and mitukattaFlg == 0:
                iterNum += 1
                randomNum = random.randrange(len(self.vocList)-1)
                if len(self.vocList[randomNum]) == 3 :
                    if self.vocList[randomNum][2][0] == _inShiritoriAnswer[2][-1:]:
                        sonzaiFlg = 0
                        for log in self.vocAnswerLogList :
                            if len(log) == 3 :
                                if log[0] == self.vocList[randomNum][0] and log[1] == self.vocList[randomNum][1] and log[2] == self.vocList[randomNum][2]:
                                    sonzaiFlg = 1
                        if sonzaiFlg == 0 :
                            vocAnswerKouhoList.append(self.vocList[randomNum])
                            if len(vocAnswerKouhoList) == 10001 :
                                mitukattaFlg = 1
            mojizemeFlg = 0
            vocAnswerKouhoList.pop(0)
            #print(vocAnswerKouhoList)

            for kouho in vocAnswerKouhoList :
                for moji in self.mojizemeList :
                    if len(kouho) == 3:
                        if kouho[2][-1:] == moji:
                            _inShiritoriAnswer = kouho
                            mojizemeFlg = 1
            if mojizemeFlg == 0:
                if len(vocAnswerKouhoList) > 0 :
                    _inShiritoriAnswer = vocAnswerKouhoList[0]

        self.vocAnswerLogList.append(_inShiritoriAnswer)
        return _inShiritoriAnswer

    def feedback(self, _inResult):
        if _inResult==1:
            hoge = 1
