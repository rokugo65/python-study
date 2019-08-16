import numpy as np
import random
import csv

class ShiritoriAiTsuyokunaru2:

    def __init__(self,_inName,_inVocList):
        self.name = _inName

        self.irekaeNum = 0
        self.taisenNum = 0
        self.makeNum = 0
        self.kachiNum = 0

        self.vocList = _inVocList
        self.vocAnswerLogList = [[]]
        self.mojizemeList = []
        self.mojizemeList_2 = []
        
        csv_file = open("mojizeme_tsuyokunaru_2.csv", "r", encoding="ms932", errors="", newline="" )
        np.f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        for row in np.f:
            self.mojizemeList.append(row)

        csv_file.close()
        del np.f

        if len(self.mojizemeList) == 75 :
            self.irekaeNum = self.mojizemeList[71]
            self.taisenNum = self.mojizemeList[72]
            self.kachiNum = self.mojizemeList[73]
            self.makeNum = self.mojizemeList[74]
            del self.mojizemeList[74]
            del self.mojizemeList[73]
            del self.mojizemeList[72]
            del self.mojizemeList[71]

        self.mojizemeList_2 = self.mojizemeList
            
        if int(self.taisenNum[0]) > 3 and float( float(self.kachiNum[0]) / float(self.taisenNum[0]) ) < 0.01:
            self.taisenNum[0] = 0
            self.makeNum[0] = 0
            self.kachiNum[0] = 0
            randomNum = random.randrange(-4,4)
            if randomNum == 0 :
                self.irekaeNum[0] = random.randrange(30)
            self.irekaeNum[0] = int(self.irekaeNum[0]) + int(randomNum)
            if self.irekaeNum[0] > 0 :
                for i in range(self.irekaeNum[0]) :
                    randomNum_1 = random.randrange(len(self.mojizemeList))
                    randomNum_2 = random.randrange(len(self.mojizemeList))
                    temp = self.mojizemeList[randomNum_1]
                    self.mojizemeList[randomNum_1] = self.mojizemeList[randomNum_2]
                    self.mojizemeList[randomNum_2] = temp
        if int(self.taisenNum[0]) > 10 and float( float(self.kachiNum[0]) / float(self.taisenNum[0]) ) < 0.40:
            self.taisenNum[0] = 0
            self.makeNum[0] = 0
            self.kachiNum[0] = 0
            randomNum = random.randrange(-4,4)
            if randomNum == 0 :
                self.irekaeNum[0] = random.randrange(30)
            self.irekaeNum[0] = int(self.irekaeNum[0]) + int(randomNum)
            if self.irekaeNum[0] > 0 :
                for i in range(self.irekaeNum[0]) :
                    randomNum_1 = random.randrange(len(self.mojizemeList))
                    randomNum_2 = random.randrange(len(self.mojizemeList))
                    temp = self.mojizemeList[randomNum_1]
                    self.mojizemeList[randomNum_1] = self.mojizemeList[randomNum_2]
                    self.mojizemeList[randomNum_2] = temp
        if int(self.taisenNum[0]) > 100 and float( float(self.kachiNum[0]) / float(self.taisenNum[0]) ) < 0.46:
            self.taisenNum[0] = 0
            self.makeNum[0] = 0
            self.kachiNum[0] = 0
            randomNum = random.randrange(-4,4)
            if randomNum == 0 :
                self.irekaeNum[0] = random.randrange(30)
            self.irekaeNum[0] = int(self.irekaeNum[0]) + int(randomNum)
            if self.irekaeNum[0] > 0 :
                for i in range(self.irekaeNum[0]) :
                    randomNum_1 = random.randrange(len(self.mojizemeList))
                    randomNum_2 = random.randrange(len(self.mojizemeList))
                    temp = self.mojizemeList[randomNum_1]
                    self.mojizemeList[randomNum_1] = self.mojizemeList[randomNum_2]
                    self.mojizemeList[randomNum_2] = temp
        if int(self.taisenNum[0]) > 200 and float( float(self.kachiNum[0]) / float(self.taisenNum[0]) ) < 0.50:
            self.taisenNum[0] = 0
            self.makeNum[0] = 0
            self.kachiNum[0] = 0
            randomNum = random.randrange(-4,4)
            if randomNum == 0 :
                self.irekaeNum[0] = random.randrange(30)
            self.irekaeNum[0] = int(self.irekaeNum[0]) + int(randomNum)
            if self.irekaeNum[0] > 0 :
                for i in range(self.irekaeNum[0]) :
                    randomNum_1 = random.randrange(len(self.mojizemeList))
                    randomNum_2 = random.randrange(len(self.mojizemeList))
                    temp = self.mojizemeList[randomNum_1]
                    self.mojizemeList[randomNum_1] = self.mojizemeList[randomNum_2]
                    self.mojizemeList[randomNum_2] = temp

        if int(self.taisenNum[0]) == 3 and float( float(self.kachiNum[0]) / float(self.taisenNum[0]) ) > 0.75:
            self.irekaeNum[0] = int(self.irekaeNum[0]) - 5
        if int(self.taisenNum[0]) == 10 and float( float(self.kachiNum[0]) / float(self.taisenNum[0]) ) > 0.66:
            self.irekaeNum[0] = int(self.irekaeNum[0]) - 5
        if int(self.taisenNum[0]) == 100 and float( float(self.kachiNum[0]) / float(self.taisenNum[0]) ) > 0.55:
            self.irekaeNum[0] = int(self.irekaeNum[0]) - 5
        if int(self.taisenNum[0]) == 200 and float( float(self.kachiNum[0]) / float(self.taisenNum[0]) ) > 0.50:
            self.irekaeNum[0] = int(self.irekaeNum[0]) - 5

    def shiritoriAI(self, _inShiritoriAnswer):
        self.vocAnswerLogList.append(_inShiritoriAnswer)
        if len(_inShiritoriAnswer) == 3 and len(self.vocList) > 0:
            iterNum = 0
            mitukattaFlg = 0
            vocAnswerKouhoList = [[]]
            while iterNum < 1500 and mitukattaFlg == 0:
                iterNum += 1
                randomNum = random.randrange(len(self.vocList)-1)
                if len(self.vocList[randomNum]) == 3 :
                    if self.vocList[randomNum][2][0] == _inShiritoriAnswer[2][-1:] :
                        sonzaiFlg = 0
                        for log in self.vocAnswerLogList :
                            if len(log) == 3 :
                                if log[0] == self.vocList[randomNum][0] and log[1] == self.vocList[randomNum][1] and log[2] == self.vocList[randomNum][2]:
                                    sonzaiFlg = 1
                        if sonzaiFlg == 0 :
                            vocAnswerKouhoList.append(self.vocList[randomNum])
                            if len(vocAnswerKouhoList) == 31 :
                                mitukattaFlg = 1
            mojizemeFlg = 0
            vocAnswerKouhoList.pop(0)

            for moji in self.mojizemeList :
                for kouho in vocAnswerKouhoList :
                    if len(kouho) == 3:
                        if kouho[2][-1:] == moji[0]:
                            _inShiritoriAnswer = kouho
                            mojizemeFlg = 1
                            break
                if mojizemeFlg == 1 :
                    break

            if mojizemeFlg == 0:
                if len(vocAnswerKouhoList) > 0 :
                    _inShiritoriAnswer = vocAnswerKouhoList[0]

        self.vocAnswerLogList.append(_inShiritoriAnswer)
        return _inShiritoriAnswer

    def feedback(self, _inResult):
        if _inResult == 1 :
            self.taisenNum[0] = int(self.taisenNum[0]) + 1
            self.kachiNum[0] = int(self.kachiNum[0]) + 1
            if self.taisenNum[0] > 300 :
                self.taisenNum[0] = int(self.taisenNum[0]) - 2
                self.kachiNum[0] = int(self.kachiNum[0]) - 1
                self.makeNum[0] = int(self.makeNum[0]) - 1
            if self.kachiNum[0] > 300 :
                self.kachiNum[0] = int(self.kachiNum[0]) - 1
                self.makeNum[0] = int(self.makeNum[0]) + 1
            self.mojizemeList.append(self.irekaeNum)
            self.mojizemeList.append(self.taisenNum)
            self.mojizemeList.append(self.kachiNum)
            self.mojizemeList.append(self.makeNum)
            f = open('mojizeme_tsuyokunaru_2.csv', 'w')
            writer = csv.writer(f, lineterminator='\n')
            print(self.mojizemeList)
            writer.writerows(self.mojizemeList)
            f.close()
        else :
            self.taisenNum[0] = int(self.taisenNum[0]) + 1
            self.makeNum[0] = int(self.makeNum[0]) + 1
            if self.taisenNum[0] > 300 :
                self.taisenNum[0] = int(self.taisenNum[0]) - 2
                self.kachiNum[0] = int(self.kachiNum[0]) - 1
                self.makeNum[0] = int(self.makeNum[0]) - 1
            if self.makeNum[0] > 300 :
                self.kachiNum[0] = int(self.kachiNum[0]) + 1
                self.makeNum[0] = int(self.makeNum[0]) - 1
            self.mojizemeList.append(self.irekaeNum)
            self.mojizemeList.append(self.taisenNum)
            self.mojizemeList.append(self.kachiNum)
            self.mojizemeList.append(self.makeNum)
            f = open('mojizeme_tsuyokunaru_2.csv', 'w')
            writer = csv.writer(f, lineterminator='\n')
            print(self.mojizemeList)
            writer.writerows(self.mojizemeList)
            f.close()
