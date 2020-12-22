





#finds the empty fields within the board (the fields with the value: 0), if there is no more empty field it returns "none" -> sudoku is solved
def findEmpty(passedBoard):
    #for loops to go through every row and column
    for i in range(len(passedBoard)):
        for j in range(len(passedBoard[0])): 
            if passedBoard[i][j] == 0: #if fields contain 0 (are empty) ...
                return (i, j)  #returns position (row, column)

    return None


#solves the board
def solve(bo):
    #finds empty fields, if there is no it returns none
    find = findEmpty(bo)

    #if there is no empty field "solve" returns "true" -> sudoku is solved
    if not find:
        return True
    #if there still are empty fields their coordinates are getting written to "row" and column"
    else:
        row, col = find

    #tries every number for that field
    for i in range(1,10):
        #checks if the number is possible, if yes the field gets set on the number
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            #recursion-step
            if solve(bo):
                return True

            #if the board isn't solved the field is getting set to 0 -> field is getting set to emtpy
            bo[row][col] = 0
    #if the algorithm can't find a solution the method returns false and the board doesn't get solved
    return False

#checks if a value in the field is possible
def valid(passedBoard, input, position):
    #checks row
    for i in range(len(passedBoard[0])):
        if passedBoard[position[0]][i] == input and position[1] != i:
            return False

    #checks column
    for i in range(len(passedBoard)):
        if passedBoard[i][position[1]] == input and position[0] != i:
            return False

    #checks 3x3 box
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if passedBoard[i][j] == input and (i,j) != position:
                return False

    #returns that the given input is possible
    return True


def start(passedBoard):
    row = 0
    column = 0
    time = -1
    # creates the 81 buttons
    for i in passedBoard:
        for j in i:
            time += 1
            # sets column to one more if needed
            column = time % 9
            # sets row to one more if needed
            if time % 9 == 0:
                row = row + 1
            # addes the button[n] on the right position
            board[row-1][column] = int(j)

    
    
    solve(board)

board = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]