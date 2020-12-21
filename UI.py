import sys
import solve
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QApplication, QVBoxLayout)


#sudoku board, 0 = empty field, you need to enter the board you want to get solved here...
board = [
        [1, 0, 0, 0, 0, 0, 0, 0, 9],
        [1, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

button = []

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
                #sets column to one more if needed
                column = time % 9
                button.append(QtWidgets.QLineEdit())
                #sets row to one more if needed
                if time % 9 == 0:
                    row = row+1

                #addes the button[n] on the right position
                layout.addWidget(button[time], row, column)

        #creates "solve" button
        solve = QtWidgets.QPushButton("Solve!")
        solve.setStyleSheet("background-color: darkblue;")
        layout.addWidget(solve, 10, 8)

        #creates an obejct of the solutionWindow and sets the solve button "clicked-funtion" to open the solutionWindow
        self.solutionWindow = solutionWindow()
        solve.clicked.connect(self.click)




        #sets window Title
        self.setWindowTitle('Sudoku Solver')

        self.show()
    
    #called when solution button is clicked
    def click(self):

        #calls solve.py and gives the board
        row = 0
        column = 0
        time = -1
        for i in button:
            time+=1
            #sets column to one more if needed
            column = time % 9
            #sets row to one more if needed
            if time % 9 == 0:
                row += 1
            if button[time].text() == "":
                board[row-1][column]=0
            else:
                board[row-1][column] = button[time].text()

        
        #opens the solutionWindow which shows the solution
        self.solutionWindow.setupUI()
        
        

class solutionWindow(QWidget):

    def setupUI(self):

        #creates GridLayout
        layout = QGridLayout()

        #sets window sizes
        self.setMinimumSize(350,250)
        self.setGeometry(700, 30, 600, 600)

        #sets the layout
        self.setLayout(layout)


        #creates content
        row = 0
        column = 0
        time = -1
        button = []
        #creates the 81 buttons
        for i in board:
            for j in i: 
                time += 1  
                #sets column to one more if needed
                column = time % 9
                button.append(QtWidgets.QPushButton(str(j)))
                #sets row to one more if needed
                if time % 9 == 0:
                    row = row+1
                #addes the button[n] on the right position
                layout.addWidget(button[time], row, column)

        





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

    def startSolutionWindow(self):
        self.solutionWindow = solutionWindow()
        self.solutionWindow.setupUI()

    



app = QApplication(sys.argv)
windowExample = MainWindow()
app.setStyleSheet(open('style.css').read()) #sets the styleSheet for the app
sys.exit(app.exec_())
