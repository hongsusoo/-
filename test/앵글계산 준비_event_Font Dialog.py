import sys
from PyQt5.QtWidgets import QWidget, QApplication,QVBoxLayout,QPushButton, QSizePolicy, QLabel, QLabel, QFontDialog
from PyQt5.QtCore import QObject, pyqtSignal

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        
        vbox = QVBoxLayout()

        btn = QPushButton('Dialog',self)
        btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        btn.move(20,20)

        vbox.addWidget(btn)
        btn.clicked.connect(self.showDialog)
        self.lbl = QLabel('스파파파파',self)
        # self.lbl.move(1000,100)

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Emit Signal")
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
