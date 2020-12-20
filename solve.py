#todo: make a gui where you can give values to each field and then let the board get solven (use pyqt5 gridlayout for that)


#sudoku board, 0 = empty field, you need to enter the board you want to get solved here...
board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#return the Board to the UI.py so that it can display it
def getBoard():
    return board


#finds the empty fields within the board (the fields with the value: 0)
def findEmpty():
    pass


#solves the board
def solve(passedBoard):
    pass

#checks if a value in the field is possible
def checkPossibility(passedBoard):
    pass




if __name__== '__main__':
    pass
