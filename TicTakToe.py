board  = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print(" Welcome to Tic Tac Toe! ")

pl1 = input(" X or O? ")

if pl1 == "X":
    pl2 = "O"
else:
     pl2 = "X"

def PlayGame(pl1, pl2):
    while True:

        response = input(" where go ")
        
        if board[int(response)] != 0:
            print(" Don't do that!! ")
        else: 
            board[int(response)] = pl1
        print(board[0],board[1],board[2])
        print(board[3],board[4],board[5])
        print(board[6],board[7],board[8])
        if board[0] == board[1] == board[2] == "X":
            print(" X wins!! ")
            return board
        elif board[3] == board[4] == board[5] == "X":
            print(" X wins!! ")
            return board
        elif board[6] == board[7] == board[8] == "X":
            print(" X wins!! ")
            return board
        elif board[0] == board[4] == board[8] == "X":
            print(" X wins!! ")
            return board
        elif board[2] == board[4] == board[6] == "X":
            print(" X wins!! ")
            return board
        elif board[0] == board[3] == board[6] == "X":
            print(" X wins!! ")
            return board
        elif board[1] == board[4] == board[7] == "X":
            print(" X wins!! ")
            return board
        elif board[2] == board[5] == board[8] == "X":
            print(" X wins!! ")
            return board
        response = input(" where go ")

        if board[int(response)] != 0:
            print(" Don't do that!! ")
        else: 
            board[int(response)] = pl2
        print(board[0],board[1],board[2])
        print(board[3],board[4],board[5])
        print(board[6],board[7],board[8])    


        if board[0] == board[1] == board[2] == "O":
            print(" O wins!! ")
            return board
        elif board[3] == board[4] == board[5] == "O":
            print(" O wins!! ")
            return board
        elif board[6] == board[7] == board[8] == "O":
            print(" O wins!! ")
            return board
        elif board[0] == board[4] == board[8] == "O":
            print(" O wins!! ")
            return board
        elif board[2] == board[4] == board[6] == "O":
            print(" O wins!! ")
            return board
        elif board[0] == board[3] == board[6] == "O":
            print(" O wins!! ")
            return board
        elif board[1] == board[4] == board[7] == "O":
            print(" O wins!! ")
            return board
        elif board[2] == board[5] == board[8] == "O":
            print(" O wins!! ")    
            return board        




PlayGame(pl1,pl2)