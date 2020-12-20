import sys
import solve
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication, QVBoxLayout)
#creates the basicwindow (hole content in here)
class basicWindow(QWidget):
    def setupUI(self):

        #creates GridLayout
        layout = QVBoxLayout()

        #sets window sizes
        self.setMinimumSize(350,250)
        self.setGeometry(0, 0, 1000, 600)

        #sets the layout
        self.setLayout(layout)


        #creates content
        labelOpen = QtWidgets.QLabel('Open')
        labelInProgress = QtWidgets.QLabel('In Progress')
        labelOpen.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        labelInProgress.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        button = QtWidgets.QPushButton('Taks')
        #addes content
        layout.addWidget(labelOpen)
        layout.addWidget(labelInProgress)
        layout.addWidget(button)

        #sets window Title
        self.setWindowTitle('Taskanizer')

        self.show()



#creates the window and calls basicWindow
class MainWindow(QWidget):
    def __init__(self):

        super(MainWindow, self).__init__()

        self.basicWindow = basicWindow()

        self.startBasicWindow()

    #starts the window
    def startBasicWindow(self):
        self.basicWindow.setupUI()



print(solve.getBoard())
app = QApplication(sys.argv)
windowExample = MainWindow()
app.setStyleSheet(open('style.css').read()) #sets the styleSheet for the app
sys.exit(app.exec_())
