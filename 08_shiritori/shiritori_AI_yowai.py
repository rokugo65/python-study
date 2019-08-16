import numpy as np
import random

class ShiritoriAiYowai:

    def __init__(self,_inName,_inVocList):
        self.name = _inName
        self.vocList = _inVocList

    def shiritoriAI(self, _inShiritoriAnswer):
        if len(_inShiritoriAnswer) == 3 and len(self.vocList) > 0:
            iterNum = 0
            mitukattaFlg = 0
            while iterNum < 3000 and mitukattaFlg == 0:
                iterNum += 1
                randomNum = random.randrange(len(self.vocList)-1)
                if len(self.vocList[randomNum]) == 3 :
                    if self.vocList[randomNum][2][0] == _inShiritoriAnswer[2][-1:] :
                        _inShiritoriAnswer = self.vocList[randomNum]
                        mitukattaFlg = 1

        return _inShiritoriAnswer

    def feedback(self, _inResult):
        if _inResult==1:
            hoge = 1
         

