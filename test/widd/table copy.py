import sys
import pandas as pd
from PyQt5.QtWidgets import QLabel, QPushButton, QTableWidget,QHeaderView,QHBoxLayout, QVBoxLayout,QWidget, QApplication,QTableWidgetItem

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.read_exl()
        self.initUI()
        self.set_exl()

    def initUI(self):
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(self.row)
        self.tableWidget.setColumnCount(self.col)

        self.label = QLabel('')
        self.addRow = QPushButton('행추가')
        self.addRow.clicked.connect(self.add_row)
        self.delRow = QPushButton('행삭제')
        self.tableWidget.cellClicked.connect(self.set_label)
        self.delRow.clicked.connect(self.del_row)
        self.clear = QPushButton('Clear')
        self.clear.clicked.connect(self.tableWidget.clear)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        

        hbox = QHBoxLayout()
        hbox.addWidget(self.addRow)
        hbox.addWidget(self.delRow)
        hbox.addWidget(self.clear)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 100, 1000, 700)
        self.show()

    def read_exl(self): #Data 불러오기
        self.df = pd.read_excel("C:/코린이/04. 개인 프로젝트/01.angle_price/data/test.xlsx",sheet_name = "a")
        self.df = self.df.dropna()
        self.col = self.df.shape[1]
        self.row = self.df.shape[0]
       
    def set_exl(self): #Data 출력
        self.tableWidget.setHorizontalHeaderLabels(self.df.columns)
        for i in range(self.row):
            for j in range(self.col):
                if type(self.df.loc[i][j])!=str: 
                    temp=str(int(self.df.loc[i][j]))+"원"
                else : temp = self.df.loc[i][j]
                self.tableWidget.setItem(i,j,QTableWidgetItem(temp))

    def add_row(self): #맨 아래 행 추가
        self.row += 1
        self.tableWidget.setRowCount(self.row)

    def del_row(self, r): #선택 행 삭제
        print(self.row)
        try:
            self.df = self.df.drop(3,axis=0)
        except Exception as e: print(e)
        except Exception as e: print(e)
        self.col = self.df.shape[1]
        self.row = self.df.shape[0]
        print(self.df)
        print(self.row)
        self.set_exl()
        
    def set_label(self, row, column): 
        item = self.tableWidget.item(row, column)
        try:
            value = item.text()
        except: 
            value = ''
        label_str = 'Row: ' + str(row+1) + ', Column: ' + str(column+1) + ', Value: ' + str(value)
        self.label.setText(label_str)
        self.r=row

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())