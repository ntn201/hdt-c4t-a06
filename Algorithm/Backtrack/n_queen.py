board = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

board = [[0 for i in range(5)] for i in range(5)]

def print_board(board):
    for row in board:
        print(row)
    print()

def check(board,row,col):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                if row == i or j == col or abs(row-i) == abs(col-j):
                    return False
    return True

def arrange(board,row=0):
    # anchor
    if row == len(board):
        print_board(board)
    if row < len(board):
        for col in range(len(board[row])):
            if check(board,row,col):
                board[row][col] = 1
                arrange(board,row+1)
                board[row][col] = 0 
        # chay qua tung cot trong row
            # kiem tra xem co bi an ko
            # neu ko -> dat hau
            # de quy
            # go hau 
        
arrange(board)