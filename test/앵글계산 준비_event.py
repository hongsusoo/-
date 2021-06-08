import sys
from PyQt5.QtWidgets import QWidget,QGridLayout, QLabel, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        grid=QGridLayout()
        grid.setSpacing(10)

        x=0
        y=0

        self.text = "x : {0}, y : {1}".format(x,y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label,0,0,Qt.AlignTop)
        self.setMouseTracking(True)
        self.setLayout(grid)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Signal and slot")
        self.show()
    
    def mouseMoveEvent(self, e):
        x=e.x()
        y=e.y()

        text = "x : {0}, y : {1}".format(x,y)
        self.label.setText(text)

    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())