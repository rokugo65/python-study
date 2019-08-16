import jaconv

class ConvertShiritori:

    def convertShiritori(self,_inStr):
        convertStr = ''
        convertStr = _inStr.replace(u'\uff0d', u'')
        convertStr = convertStr.replace(u'\uff5e', u'')

        convertStr = jaconv.hira2kata(convertStr)
        convertStr = convertStr.replace(u'ヴァ', u'バ')
        convertStr = convertStr.replace(u'ヴィ', u'ビ')
        convertStr = convertStr.replace(u'ヴ', u'ブ')
        convertStr = convertStr.replace(u'ヴェ', u'ベ')
        convertStr = convertStr.replace(u'ヴォ', u'ボ')
        convertStr = convertStr.replace(u'ヱ', u'エ')
        convertStr = convertStr.replace(u'ヂ', u'ジ')
        convertStr = convertStr.replace(u'ヅ', u'ズ')
        convertStr = convertStr.replace(u'ヲ', u'オ')

        convertStr = self.convertHanon(convertStr)
        _outStr = self.convertChouonpu(convertStr)

        return _outStr

    def convertHanon(self,_inStr):
        _outStr = _inStr
        _outStr = _outStr.replace("ぁ","あ")
        _outStr = _outStr.replace("ぃ","い")
        _outStr = _outStr.replace("ぅ","う")
        _outStr = _outStr.replace("ぇ","え")
        _outStr = _outStr.replace("ぉ","お")
        _outStr = _outStr.replace("っ","つ")
        _outStr = _outStr.replace("ゃ","や")
        _outStr = _outStr.replace("ゅ","ゆ")
        _outStr = _outStr.replace("ょ","よ")
        _outStr = _outStr.replace("ァ","ア")
        _outStr = _outStr.replace("ィ","イ")
        _outStr = _outStr.replace("ゥ","ウ")
        _outStr = _outStr.replace("ェ","エ")
        _outStr = _outStr.replace("ォ","オ")
        _outStr = _outStr.replace("ッ","ツ")
        _outStr = _outStr.replace("ャ","ヤ")
        _outStr = _outStr.replace("ュ","ユ")
        _outStr = _outStr.replace("ョ","ヨ")

        return _outStr


    def convertChouonpu(self,_inStr):
        _outStr = _inStr
        chouonpuIndex = -2
        while chouonpuIndex != -1:
            chouonpuIndex = _outStr.find('ー')
            if chouonpuIndex != -1:
                if chouonpuIndex == 0:
                    strList = list(_outStr)
                    strList.pop(chouonpuIndex)
                    _outStr = "".join(strList)
                elif chouonpuIndex >= 1:
                    strList = list(_outStr)
                    if self.isAgyou(strList[chouonpuIndex-1]):
                        strList[chouonpuIndex] = 'ア'
                    elif self.isIgyou(strList[chouonpuIndex-1]):
                        strList[chouonpuIndex] = 'イ'
                    elif self.isUgyou(strList[chouonpuIndex-1]):
                        strList[chouonpuIndex] = 'ウ'
                    elif self.isEgyou(strList[chouonpuIndex-1]):
                        strList[chouonpuIndex] = 'エ'
                    elif self.isOgyou(strList[chouonpuIndex-1]):
                        strList[chouonpuIndex] = 'オ'
                    elif strList[chouonpuIndex-1] == 'ン':
                        strList[chouonpuIndex] = 'ン'
                    else :
                        strList.pop(chouonpuIndex)
                    _outStr = "".join(strList)

        return _outStr

    def isAgyou(self,_inStr):
        initial = _inStr[:1]
        agyouFlg = 0

        agyouStr = 'あかさたなはまやらわがざだばぱぁゃアカサタナハマヤラワガザダバパァャ'
        if agyouStr.find(initial) > -1:
            agyouFlg = 1

        return agyouFlg

    def isIgyou(self,_inStr):
        initial = _inStr[:1]
        igyouFlg = 0

        igyouStr = 'いきしちにひみいりいぎじぢびぴぃイキシチニヒミイリイギジヂビピィ'
        if igyouStr.find(initial) > -1:
            igyouFlg = 1

        return igyouFlg

    def isUgyou(self,_inStr):
        initial = _inStr[:1]
        ugyouFlg = 0

        ugyouStr = 'うくすつぬふむゆるうぐずづぶぷぅっゅウクスツヌフムユルウグズヅブプゥッュヴ'
        if ugyouStr.find(initial) > -1:
            ugyouFlg = 1

        return ugyouFlg

    def isEgyou(self,_inStr):
        initial = _inStr[:1]
        egyouFlg = 0

        egyouStr = 'えけせてねへめえれえげぜでべぺぇエケセテネヘメエレエゲゼデベペェ'
        if egyouStr.find(initial) > -1:
            egyouFlg = 1

        return egyouFlg

    def isOgyou(self,_inStr):
        initial = _inStr[:1]
        ogyouFlg = 0

        ogyouStr = 'おこそとのほもよろおごぞどぼぽぉょオコソトノホモヨロオゴゾドボポォョ'
        if ogyouStr.find(initial) > -1:
            ogyouFlg = 1

        return ogyouFlg

if __name__ == "__main__":
    print('変換したい文字列を入力してください')
    inputStr = input()
    convShiri = ConvertShiritori()
    outputStr = convShiri.convertShiritori(inputStr)
    print(outputStr)