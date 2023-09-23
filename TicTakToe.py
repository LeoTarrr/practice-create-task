board  = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print(" Welcome to Tic Tac Toe! ")

pl1 = input(" X or O? ")

if pl1 == "X":
    pl2 = "O"
else:
     pl2 = "X"
def PlayGame(numrounds):
    while True:

        response = input(" where go ")
        #numbers = [1,asdfghjk,]
        if board[int(response)] != 0:
            print(" Don't do that!! ")
        else: 
            board[int(response)] = pl1
        print(board[0],board[1],board[2])
        print(board[3],board[4],board[5])
        print(board[6],board[7],board[8])

        response = input(" where go ")

        if board[int(response)] != 0:
            print(" Don't do that!! ")
        else: 
            board[int(response)] = pl2
        print(board[0],board[1],board[2])
        print(board[3],board[4],board[5])
        print(board[6],board[7],board[8])    

        if board[0] and board[1] and board[2] == "X":
            print(" X wins!! ")
        elif board[3] and board[4] and board[5] == "X":
            print(" X wins!! ")
        elif board[6] and board[7] and board[8] == "X":
            print(" X wins!! ")
        elif board[0] and board[4] and board[8] == "X":
            print(" X wins!! ")
        elif board[2] and board[4] and board[6] == "X":
            print(" X wins!! ")
        elif board[0] and board[3] and board[6] == "X":
            print(" X wins!! ")
        elif board[1] and board[4] and board[7] == "X":
            print(" X wins!! ")
        elif board[2] and board[5] and board[8] == "X":
            print(" X wins!! ")
        elif board[0] and board[1] and board[2] == "O":
            print(" O wins!! ")
        elif board[3] and board[4] and board[5] == "O":
            print(" O wins!! ")
        elif board[6] and board[7] and board[8] == "O":
            print(" O wins!! ")
        elif board[0] and board[4] and board[8] == "O":
            print(" O wins!! ")
        elif board[2] and board[4] and board[6] == "O":
            print(" O wins!! ")
        elif board[0] and board[3] and board[6] == "O":
            print(" O wins!! ")
        elif board[1] and board[4] and board[7] == "O":
            print(" O wins!! ")
        elif board[2] and board[5] and board[8] == "O":
            print(" O wins!! ")            

PlayGame(3)
PlayGame(5)

