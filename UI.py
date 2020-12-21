import sys
import solve
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication, QVBoxLayout)
#creates the basicwindow (hole content in here)
class basicWindow(QWidget):
    def setupUI(self):

        #creates GridLayout
        layout = QGridLayout()

        #sets window sizes
        self.setMinimumSize(350,250)
        self.setGeometry(0, 0, 600, 600)

        #sets the layout
        self.setLayout(layout)


        #creates content
        row = 0
        column = 0
        time = -1
        #creates the 81 buttons
        for i in board:
            for j in i: 
                time += 1  
                #sets column to % of 3
                column = time % 9
                button = QtWidgets.QPushButton(str(j))
                #checks if i is 3*n and if it is it adds 1 to row
                if time % 9 == 0:
                    row = row+1
                layout.addWidget(button, row, column)
                
              
       
       

        #sets window Title
        self.setWindowTitle('Sudoku Solver')

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



board = solve.getBoard()
app = QApplication(sys.argv)
windowExample = MainWindow()
app.setStyleSheet(open('style.css').read()) #sets the styleSheet for the app
sys.exit(app.exec_())
