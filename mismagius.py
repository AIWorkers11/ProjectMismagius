class Mismagius:
    def __init__(self):
        self.modelname = "ムウマージ"
        self.modelposx = 0
        self.modelposy = 0
        self.sendmes = ""

    def send(self,text):
        positive_word = ["好き","スキ","好きだよ"]
        hyper_positive_word = ["大好き","ダイスキ"]
        negative_word = ["嫌い","キライ","嫌い"]
        hyper_negative_word = ["大嫌い"]

        if text in positive_word:
            self.sendmes = "む！"
        elif text in hyper_positive_word:
            self.sendmes = "♪～"
        elif text in negative_word:
            self.sendmes = "まぁじ……"
        elif text in hyper_negative_word: 
            self.sendmes = "……"
        else:
            self.sendmes = "むぅ？"
        

    def getModelName(self):
        return self.modelname
    
    def getModelPosX(self):
        return self.modelposx

    def getModelPosY(self):
        return self.modelposy
    
    def getSendMessage(self):
        return self.sendmes

    def setModelPosX(self,x):
        self.modelposx = x

    def setModelPosY(self,y):
        self.modelposy = y