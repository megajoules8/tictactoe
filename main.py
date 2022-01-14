#tictactoe against ai

board = [' ' for x in range(10)] 

def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def insertBoard(letter, pos): #call this, give it letter and position to play
     board[pos] = letter

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos): #check if space is free
    return board[pos] == ' '

# This function will return a True or False value




def isWinner(currentBoard, letterUsed ): #checks to see if letter on current board in each space is the same letter in a winning combination
#returns true if player has won
    return ((currentBoard[7] == letterUsed and currentBoard[8] == letterUsed and currentBoard[9] == letterUsed) or # across the top
      (currentBoard[4] == letterUsed and currentBoard[5] == letterUsed and currentBoard[6] == letterUsed) or # across the middle
      (currentBoard[1] == letterUsed and currentBoard[2] == letterUsed and currentBoard[3] == letterUsed) or # across the bottom
      (currentBoard[7] == letterUsed and currentBoard[4] == letterUsed and currentBoard[1] == letterUsed) or # down the left side
      (currentBoard[8] == letterUsed and currentBoard[5] == letterUsed and currentBoard[2] == letterUsed) or # down the middle
      (currentBoard[9] == letterUsed and currentBoard[6] == letterUsed and currentBoard[3] == letterUsed) or # down the right side
      (currentBoard[7] == letterUsed and currentBoard[5] == letterUsed and currentBoard[3] == letterUsed) or # diagonal
      (currentBoard[9] == letterUsed and currentBoard[5] == letterUsed and currentBoard[1] == letterUsed)) # diagonal

def playerMove():
    run = True
    while run:  # Keep looping until we get a valid move
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move  = int(move)
            if move > 0 and move < 10:  #checks typed in a number between 1-9
                if spaceIsFree(move):  # check if move is valid 
                    run = False
                    insertBoard('X', move)
                else:
                    print('This postion is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] # Create a list of possible moves
    move = 0
    
    #Check for possible winning move to take or to block opponents winning move
    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move


    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    #Try to take the center
    if 5 in possibleMoves:
        move = 5
        return move

    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    

    
def isBoardFull(board):
    if board.count(' ') > 1:  # Since always one blank element in board, must use > 1
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, you lose!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('You Win! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break