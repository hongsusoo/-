import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout, QLabel, QApplication,QTextEdit

class Example(QWidget): 
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.btn = QPushButton("text 가져오기",self)
        self.btn.clicked.connect(self.initUI) #특정 상황에서 메소드 사용시 () 사용X
        print(self.get_text())                #무조건 사용될때 () 사용?
        self.btn.setGeometry(350,10,140,40)
        self.textEdit.setGeometry(10,10,300,300)
        self.setGeometry(300,300,500,500)
        self.setWindowTitle("Signal and Slot")
        self.show()
    def get_text(self):
        return self.textEdit.toPlainText()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    a = Example()
    ex = Example().get_text()
    print(ex,"처음")
    sys.exit(app.exec_())
