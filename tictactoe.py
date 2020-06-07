#Implementation of Two player tictactoe game in python

board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' ' }
board_keys = []
for key in board:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def game():
    turn = 'X'
    count = 0
    isDone = False
    for i in range(10):
        printBoard(board)
        print("It's " + turn + " turn. enter a number to place your piece")
        move = input()
        if(board[move] == ' '):
            board[move] = turn
            count += 1
        else:
            print("The location is filled please enter a different location")
            continue
        if (count >= 5):

            if (board['7'] == board['8'] == board['9'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif(board['4'] == board['5'] == board['6'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif(board['1'] == board['2'] == board['3'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                break
            elif(board['1'] == board['4'] == board['7'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif(board['2'] == board['5'] == board['8'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif(board['3'] == board['6'] == board['9'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif(board['7'] == board['5'] == board['3'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif(board['1'] == board['5'] == board['9'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
        if count == 9:
            print("Game Over\n")
            print("It's a tie!!")
            isDone = True
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        if isDone:
            restart = input("Do you want to play again? (y/n)")

            if (restart == 'y'):
                isDone = False
                for key in board_keys:
                    board[key] = " "
                game()
if __name__=="__main__":
    game()