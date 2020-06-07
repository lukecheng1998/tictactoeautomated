import numpy as np
from random import randint, shuffle
from random import seed
from time import sleep
board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' ' }
board_keys = []
seed(10)
for key in board:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def game():
    isDone = False
    getRandom = randint(0,10)
    count = 0
    print(getRandom)
    turn = 'X'
    if(getRandom > 5):
        turn = '0'
    if(turn == 'X'):
        print("human's start")
    else:
        print("AIs start")
    for i in range(10):
        printBoard(board)

        if (turn == 'X'):
            print("It's " + turn + " turn. enter a number to place your piece")
            while(1):
                move = input()
                if board[move] == ' ':
                    count += 1
                    board[move] = turn

                    break
                else:
                    print("The location is filled please enter a different location")
                    continue


        else:
            print("It's " + turn + " turn. The AI will place a piece")
            sequence = [i for i in range(1, 10)]
            shuffle(sequence)
            print(sequence)

            for i in range(0, 10):
                s = str(sequence[i])
                move = s
                if board[move] == ' ':
                    count += 1
                    board[move] = turn

                    break
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
            elif (board['4'] == board['5'] == board['6'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif (board['1'] == board['2'] == board['3'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                break
            elif (board['1'] == board['4'] == board['7'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif (board['2'] == board['5'] == board['8'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif (board['3'] == board['6'] == board['9'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif (board['7'] == board['5'] == board['3'] != ' '):
                printBoard(board)
                print("\n GameOver. \n")
                print("**** " + turn + " won")
                isDone = True
                break
            elif (board['1'] == board['5'] == board['9'] != ' '):
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
            turn = '0'
        else:
            turn = 'X'

if __name__=="__main__":
    game()