import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication,QFrame,QColorDialog, QApplication,QFontDialog, QCheckBox
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        col = QColor(0,0,0)

        btn = QPushButton('Dialog',self)
        btn.move(20,20)
        
        btn.clicked.connect(self.showDialog)
        print(col.name())

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color : %s}"%col.name())
        self.frm.setGeometry(130,22,100,100)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Color Dialog")
        self.show()

    def showDialog(self):
        col= QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color : %s}"%col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
