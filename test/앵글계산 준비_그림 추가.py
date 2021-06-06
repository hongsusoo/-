import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication,QFrame,QColorDialog, QApplication,QFontDialog, QCheckBox,QHBoxLayout
from PyQt5.QtGui import QColor,QPixmap
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        hbox=QHBoxLayout(self)
        pixmap=QPixmap()
        pixmap.load('C:/코린이/04. 개인 프로젝트/앵글계산/dog.jpg')
        # pixmap.scaledToWidth(300)
        # pixmap.scaledToHeight(300)
        lbl=QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.setGeometry(300,300,1000,1000)
        self.setWindowTitle("Color Dialog")
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckbox')
        else : 
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
