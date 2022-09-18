from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QFont

class Calc(QMainWindow):
    def __init__(self):
        super(Calc,self).__init__()
        uic.loadUi("Calculator.ui",self)
        self.show()

        self.sevenButton.clicked.connect(self.type_7)
        self.eightButton.clicked.connect(self.type_8)
        self.nineButton.clicked.connect(self.type_9)
        self.zeroButton.clicked.connect(self.type_0)
        self.oneButton.clicked.connect(self.type_1)
        self.twoButton.clicked.connect(self.type_2)
        self.threeButton.clicked.connect(self.type_3)
        self.fourButton.clicked.connect(self.type_4)
        self.fiveButton.clicked.connect(self.type_5)
        self.sixButton.clicked.connect(self.type_6)
        self.plusminusButton.clicked.connect(self.delete)
        self.dotButton.clicked.connect(self.dot)
        self.plusButton.clicked.connect(self.plus)
        self.minusButton.clicked.connect(self.minus)
        self.multiplyButton.clicked.connect(self.multiply)
        self.divisionButton.clicked.connect(self.division)
        self.cButton.clicked.connect(self.clear)
        self.equalButton.clicked.connect(self.equal)
        
        

    def type_7(self,msg):
        if self.outputLabel.text()=='0':
            self.outputLabel.setText('7')
        else:
            text=self.outputLabel.text()
            self.outputLabel.setText(text+'7')

    def type_8(self):
        if self.outputLabel.text()=='0':
            self.outputLabel.setText('8')
        else:
            text=self.outputLabel.text()
            self.outputLabel.setText(text+'8')

    def type_9(self):
        if self.outputLabel.text()=='0':
            self.outputLabel.setText('9')
        else:
            text=self.outputLabel.text()
            self.outputLabel.setText(text+'9')

    def type_1(self):
        if self.outputLabel.text()=='0':
            self.outputLabel.setText('1')
        else:
            text=self.outputLabel.text()
            self.outputLabel.setText(text+'1')

    def type_2(self):
        if self.outputLabel.text()=='0':
            self.outputLabel.setText('2')
        else:
            text=self.outputLabel.text()
            self.outputLabel.setText(text+'2')

    def type_3(self):
        if self.outputLabel.text()=='0':
            self.outputLabel.setText('3')
        else:
            text=self.outputLabel.text()
            self.outputLabel.setText(text+'3')

    def type_4(self):
        if self.outputLabel.text()=='0':
            self.outputLabel.setText('4')
        else:
            text=self.outputLabel.text()
            self.outputLabel.setText(text+'4')

    def type_5(self):
        if self.outputLabel.text()=='0':
            self.outputLabel.setText('5')
        else:
            text=self.outputLabel.text()
            self.outputLabel.setText(text+'5')

    def type_6(self):
        if self.outputLabel.text()=='0':
            self.outputLabel.setText('6')
        else:
            text=self.outputLabel.text()
            self.outputLabel.setText(text+'6')

    def type_0(self):
        if self.outputLabel.text()=='0':
            self.outputLabel.setText('0')
        else:
            text=self.outputLabel.text()
            self.outputLabel.setText(text+'0')
        
    def delete(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text[:len(text)-1])

    def dot(self):
        text=self.outputLabel.text()
        self.outputLabel.setText(text+'.')

    def plus(self):
        text=self.outputLabel.text()
        self.outputLabel.setText(text+'+') 

    def minus(self):
        text=self.outputLabel.text()
        self.outputLabel.setText(text+'-')

    def multiply(self):
        text=self.outputLabel.text()
        self.outputLabel.setText(text+'*')

    def division(self):
        text=self.outputLabel.text()
        self.outputLabel.setText(text+'/')

    def clear(self):
        self.outputLabel.setText('0')

    def equal(self):
        equation=self.outputLabel.text()

        try:
            ans=eval(equation)
            self.outputLabel.setText(str(ans))
        except:
            self.outputLabel.setText("Wrong Input")
            self.outputLabel.setFont(QFont("Arial",16))

def main():
    app = QApplication([])
    window = Calc()
    app.exec_()
    

if __name__=='__main__' :
    main()


