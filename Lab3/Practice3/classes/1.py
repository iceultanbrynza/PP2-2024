class ActionsOnStrings:
    def __init__(self):
        self.strs = ""
    def getString(self):
        self.strs = input()
    def printString(self):
        print(self.strs.upper())

stroka = ActionsOnStrings()
stroka.getString()
stroka.printString()