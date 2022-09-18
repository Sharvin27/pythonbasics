from email import message
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
# def main():
#     app = QApplication([])
#     window = QWidget()
#     window.setGeometry(300,100,700,500)         #(x,y,size,size)
#     window.setWindowTitle("My simple GUI")

#     label = QLabel(window)
#     label.setText("Hello World")
#     label.setFont(QFont("Arial",16))
#     label.move(45,100)
#     window.show()
#     app.exec_()

# if __name__ =='__main__':
#     main()




# def main():
#     app = QApplication([])
#     window = QWidget()
#     window.setGeometry(200,400,500,400)
#     window.setWindowTitle("MY FIRST GUI")

#     layout =QVBoxLayout()

#     label = QLabel("Press the button below")
#     textbox = QTextEdit()
#     button = QPushButton("Press me!")

#     button.clicked.connect(lambda:on_clicked(textbox.toPlainText()))

#     layout.addWidget(label)
#     layout.addWidget(textbox)
#     layout.addWidget(button)

#     window.setLayout(layout)

#     window.show()
#     app.exec_()

# def on_clicked(msg):
#     # print("Hello World")
#     message = QMessageBox()
#     message.setText(msg)
#     message.exec_()

# if __name__ == '__main__':
#     main()




from PyQt5 import uic                                               #with QtDesigner

class MyGui(QMainWindow):
    def __init__(self):
        super(MyGui,self).__init__()
        uic.loadUi("mygui.ui",self)
        self.show()

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(lambda:self.sayit(self.textEdit.toPlainText()))
        self.actionClose.triggered.connect(exit)

    def login(self):
        if self.lineEdit.text()=="Sharvin" and self.lineEdit_2.text()=="12345678":
            self.textEdit.setEnabled(True)
            self.pushButton_2.setEnabled(True)
        else:
            message=QMessageBox()
            message.setText("Invalid Login!")
            message.exec_()

    def sayit(self,msg):
        message=QMessageBox()
        message.setText(msg)
        message.exec_()


def main():
    app = QApplication([])
    window = MyGui()
    app.exec_()
    

if __name__=='__main__' :
    main()

