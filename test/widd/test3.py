import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

CalUI = 'test/UIfiles/angle_price.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(CalUI,self)
        self.input_toolButton.clicked.connect(self.input_text)


    def input_text(self):
        print("클릭스")
        print(self.q_lineEdit.text())


app = QApplication(sys.argv)
main = MainDialog()
main.show()
app.exec_()

