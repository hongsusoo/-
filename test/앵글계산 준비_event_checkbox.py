import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication,QFrame,QColorDialog, QApplication,QFontDialog, QCheckBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        cb = QCheckBox('Show Title', self)
        cb2 = QCheckBox('Show Title2' self)

        cb.move(20,20)
        cb2.move(20,40)
        # cb.toggle()
        cb2.toggle()
        
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300,300,250,150)
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
