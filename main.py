from my_chess import *
from random import randint
import math


def minimax(board_copy, depth, alpha, beta, maximizingPlayer):
    if depth == 0:  # or game over
        print("Returning with worth: ", board_copy.calculate_Board_Worth())
        return board_copy.calculate_Board_Worth(), board_copy  # Static eval of position
    moves = board_copy.legal_moves()
    board_copy.print_ChessBoard()
    if maximizingPlayer == True:
        print("Max depth", depth)
        maxEval = -math.inf
        best_board = {}
        for move in moves:
            board_copy.push(move)
            eval, new_board = minimax(board_copy, depth-1, alpha, beta, False)

            if maxEval < eval:
                best_board = new_board

            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            board_copy.pop()
            if beta <= alpha:
                break
        return maxEval, best_board
    else:
        minEval = +math.inf
        print("Min depth", depth)
        for move in moves:
            board_copy.push(move)
            eval, new_board = minimax(board_copy, depth-1, alpha, beta, True)

            if minEval > eval:
                best_board = new_board

            minEval = min(minEval, eval)
            beta = min(beta, eval)
            board_copy.pop()
            if beta <= alpha:
                break
        return minEval, best_board


def main():
    b = Board()

    # while True:
    #     x = b.legal_moves()
    #     if b.check_Mate == True:
    #         print("\n\n~~~~~~ CHECKMATE ~~~~~~")
    #         break
    #     print(x)
    #     print("BOARD WORTH TURN: ", b.calculate_Board_Worth())
    #     b.print_ChessBoard()
    #     b.move_From(x[randint(0, len(x)-1)])
    #     b.print_ChessBoard()

    # print(b.history)
    board_copy = b
    eval, b1 = minimax(board_copy, 3, -math.inf, +math.inf, True)
    board_copy.print_ChessBoard()
    b1.print_ChessBoard()


main()
