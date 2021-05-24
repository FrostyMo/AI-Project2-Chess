from typing import NamedTuple
import chess
from chess import *
from collections import namedtuple
# Create a board of size 8x8
BOARD = {}

# "king": 1
# "queen": 2
# "knight": 3
# "bishop": 4
# "rook": 5
# "pawn": 6

TWO_BOARD = [[5, 3, 4, 2, 1, 4, 3, 5],
             [6, 6, 6, 6, 6, 6, 6, 6],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [6, 6, 6, 6, 6, 6, 6, 6],
             [5, 3, 4, 2, 1, 4, 3, 5]
             ]

LIST_BOARD = []


def create_Board():
    global BOARD
    global TWO_BOARD
    global LIST_BOARD

    a = ord('a')
    n = ord('8')
    alph = [chr(i) for i in range(a, a+8)]
    numbers = [chr(i) for i in range(n, n-8, -1)]
    print(numbers)
    print(alph)
    Position = namedtuple('Position', ['row', 'column'])

    p = Position(2, 'a')
    print(p, p.row, p.column)

    for i_index, i in enumerate(numbers):
        mylist = []
        for j_index, j in enumerate(alph):
            if (TWO_BOARD[i_index][j_index] == 0):
                BOARD[j+i] = "Empty"
            elif (TWO_BOARD[i_index][j_index] == 1):
                BOARD[j+i] = "King"
            elif (TWO_BOARD[i_index][j_index] == 2):
                if (i == '8' or j+i == 'd4'):
                    BOARD[j+i] = Queen("Queen", j+i, "Black")
                else:
                    BOARD[j+i] = Queen("Queen", j+i, "White")
            elif (TWO_BOARD[i_index][j_index] == 3):
                if (i == '8'):
                    BOARD[j+i] = Knight("Knight", j+i, "Black")
                else:
                    BOARD[j+i] = Knight("Knight", j+i, "White")
            elif (TWO_BOARD[i_index][j_index] == 4):

                if (i == '8'):
                    BOARD[j+i] = Bishop("Bishop", j+i, "Black")
                else:
                    BOARD[j+i] = Bishop("Bishop", j+i, "White")
            elif (TWO_BOARD[i_index][j_index] == 5):
                if (i == '8' or j+i == 'd4'):
                    BOARD[j+i] = Rook("Rook", j+i, "Black")
                else:
                    BOARD[j+i] = Rook("Rook", j+i, "White")
            elif (TWO_BOARD[i_index][j_index] == 6):
                if (i == '7'):
                    BOARD[j+i] = Pawn("Pawn", j+i, "Black")
                else:
                    BOARD[j+i] = Pawn("Pawn", j+i, "White")
            mylist.append(j+i)
        LIST_BOARD.append(mylist)
    print_Board()
    print(LIST_BOARD)
    print(index_2d(LIST_BOARD, 'a7'))


def print_Board():
    global BOARD

    for i, key in enumerate(BOARD):
        print("['{}': ".format(key), BOARD[key], end="] ")
        if (i+1) % 8 == 0 and i != 0:
            print("")


def main():
    create_Board()
    pawn = Pawn("Pawn", "a7", "Black")
    pawn.moves_Available(LIST_BOARD, BOARD)

    print("Pawn 1 can move to: ", pawn.moves)

    pawn = Pawn("Pawn", "e7", "Black")
    pawn.moves_Available(LIST_BOARD, BOARD)

    print("Pawn 2 can move to: ", pawn.moves)

    pawn = Pawn("Pawn", "c3", "Black")
    pawn.moves_Available(LIST_BOARD, BOARD)

    print("Pawn 3 can move to: ", pawn.moves)

    r1 = Queen("Queen", "d4", "Black")
    r1.moves_Available(LIST_BOARD, BOARD)

    print("Queen 1 can move to: ", r1.moves)


main()
