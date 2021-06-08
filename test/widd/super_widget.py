import sys
import Test
from PyQt5.QtWidgets import QApplication


app=QApplication(sys.argv)
ex = Test.Example()
sys.exit(app.exec_())

