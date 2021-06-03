import sys
from PyQt5.QtWidgets import QApplication, QPushButton,QWidget,QMessageBox,QMainWindow,QAction,QMenu,qApp,QLabel,QApplication,QHBoxLayout, QVBoxLayout


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        a=QMainWindow.statusBar()
        self.a #상태창
        self.a.showMessage("안녕하세요!")
        menu = self.menuBar() # 메뉴바 _ 메뉴생성
        menu_file = menu.addMenu('File') # 그룹생성
        menu_edit = menu.addMenu('Edit') # 그룹생성
        menu_view = menu.addMenu('View') # 그룹생성

        file_exit = QAction('Exit',self) # 메뉴 객체 생성_메모리만 생성_ action이 가능한 객체 생성
        file_exit.setShortcut('Ctrl+Q')
        file_exit.setStatusTip('누르면 안녕')
        new_txt = QAction("텍스트파일",self)
        new_py = QAction("파이썬 파일",self)
        view_stat = QAction('상태표시줄', self, checkable = True)
        view_stat.setChecked(True)

        file_exit.triggered.connect(qApp.quit)
        view_stat.triggered.connect(self.tglStat)

        file_new=QMenu('New',self) #서브 그룹

        file_new.addAction(new_txt) #서브 메뉴 추가
        file_new.addAction(new_py)  #서브 메뉴 추가


        menu_file.addMenu(file_new)    # 메인 메뉴 추가
        menu_file.addAction(file_exit) # 메인 메뉴 추가
        menu_view.addAction(view_stat)

        btn = QPushButton('종료',self)

        # btn.resize(btn.sizeHint())
        btn.setToolTip("툴팁입니다. <b> 안녕하세요!<b/>")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        # btn.move(30,50)
        btn.clicked.connect(qApp.quit) #이벤트 처리

        self.setLayout(vbox)
        # self.setGeometry(500,500,400,600)
        self.setWindowTitle("앵글가격계산표")
        self.show()
    
    def closeEvent(self, QCloseEvent):
        ans = QMessageBox.question(self, "종료 확인", "종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes :
            QCloseEvent.accept()
        else :
            QCloseEvent.ignore()
    def tglStat(self, state):
        if state:
            self.statusBar().show()
        else : 
            self.statusBar().hide()

    def contextMenuEvent(self, QContextMenuEvent):
        cm=QMenu(self)

        quit = cm.addAction("Quit")
        action= cm.exec_(self.mapToGlobal(QContextMenuEvent.pos()))
        if action == quit:
            qApp.quit()



app=QApplication(sys.argv)
w=Exam()
sys.exit(app.exec_()) #이벤트 처리를 위한 루프를 실행(Mainloop)``