import sys
import numpy as np
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_rand_int()

    def initUI(self):
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(4)

        self.label = QLabel('')

        self.scrollToTop = QPushButton('Scroll to Top')
        self.scrollToTop.clicked.connect(self.tableWidget.scrollToTop)
        self.scrollToBottom = QPushButton('Scroll to Bottom')
        self.scrollToBottom.clicked.connect(self.tableWidget.scrollToBottom)
        self.setItems = QPushButton('Set Items')
        self.setItems.clicked.connect(self.set_rand_int)
        self.clear = QPushButton('Clear')
        self.clear.clicked.connect(self.tableWidget.clear)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.cellClicked.connect(self.set_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.scrollToTop)
        hbox.addWidget(self.scrollToBottom)
        hbox.addWidget(self.setItems)
        hbox.addWidget(self.clear)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()

    def set_rand_int(self):
        rand_int = np.random.randint(1, 100, size=(20, 4))
        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(rand_int[i, j])))

    def set_label(self, row, column):
        item = self.tableWidget.item(row, column)
        value = item.text()
        label_str = 'Row: ' + str(row+1) + ', Column: ' + str(column+1) + ', Value: ' + str(value)
        self.label.setText(label_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())