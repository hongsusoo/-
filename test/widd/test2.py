import sys
from PyQt5.QtWidgets import QWidget,QGridLayout, QLabel, QApplication,QMainWindow,QToolButton,QSizePolicy

from PyQt5.QtCore import Qt



class Button(QToolButton):
    def __init__(self, text):
        super().__init__()
        buttonStyle = '''
        QToolButton:hover {border:1px solid #0078d7; background-color:#e5f1fb;}
        QToolButton:pressed {background-color:#a7c8e3}
        QToolButton {font-size:11pt; font-family:NaNum Gothic; border:1px solid #d6d7d8; background-color#f0f1f1}
        '''
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred) #버튼의 사이즈 정책을 결정.
        self.setText(text)
        self.setStyleSheet(buttonStyle)
    
    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 30)
        size.setWidth(max(size.width(), size.height()))
        return size

class App(QMainWindow):
    def __init__(self): 
        super().__init__() 
        
        self.title = "계산기"
        self.setWindowTitle(self.title)

        self.b=Button("비어튼").sizeHint()


        self.left = 100
        self.top = 200
        self.width = 300
        self.height = 200
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

app = QApplication([])
calc = App()
app.exec_()

