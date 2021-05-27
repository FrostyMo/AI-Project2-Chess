from my_chess import *
from random import randint


def main():
    b = Board()

    while True:
        x = b.legal_moves()
        if b.check_Mate == True:
            print("\n\n~~~~~~ CHECKMATE ~~~~~~")
            break
        print(x)
        print("BOARD WORTH TURN: ", b.calculate_Board_Worth())
        b.move_From(x[randint(0, len(x)-1)])
        b.print_ChessBoard()

    print(b.history)


main()
