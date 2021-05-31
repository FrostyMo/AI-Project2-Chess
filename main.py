from my_chess import *
from random import randint
from copy import deepcopy
import math


def minimax(board_copy, depth, alpha, beta, maximizingPlayer, move_count):
    if depth == 0:  # or game over
        # print("Returning with worth: ", board_copy.calculate_Board_Worth())
        # Static eval of position
        return board_copy.calculate_Board_Worth(), deepcopy(board_copy)
    # board_copy.print_ChessBoard()
    moves = board_copy.legal_moves()

    if maximizingPlayer == True:
        # print("Max depth", depth)
        maxEval = -math.inf
        best_board = None
        for move in moves:
            board_copy.push(move)
            eval, new_board = minimax(
                board_copy, depth-1, alpha, beta, False, move_count)

            if maxEval < eval:
                # print("Choosing best max")
                best_board = new_board
                # best_board.print_ChessBoard()
            else:
                if len(best_board.last_move) > move_count:
                    best_board.pop()
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            board_copy.pop()
            if beta <= alpha:
                # best_board = new_board
                break
        # print("Before returning maximum: ~~~~")
        # best_board.print_ChessBoard()
        return maxEval, best_board
    else:
        minEval = +math.inf
        #print("Min depth", depth)
        best_board = None
        for move in moves:
            board_copy.push(move)
            eval, new_board = minimax(
                board_copy, depth-1, alpha, beta, True, move_count)

            if minEval > eval:
                # print("Choosing best min")
                best_board = new_board
                # best_board.print_ChessBoard()
            else:
                if len(best_board.last_move) > move_count:
                    best_board.pop()
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            board_copy.pop()
            if beta <= alpha:
                # best_board = new_board
                break
        # print("Before returning minimum: ~~~~")
        # best_board.print_ChessBoard()
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
    b1 = board_copy
    for i in range(30):
        eval, b1 = minimax(b1, 3, -math.inf, +math.inf, True, i+1)
        # board_copy.print_ChessBoard()
        # b1.print_ChessBoard()
        # moves = b1.legal_moves()
        # print(moves)
        # while True:
        #     new_move = input("Please enter your move (e.g a2a4): ")
        #     if new_move in moves:
        #         b1.move_From(new_move)
        #         break
        #     else:
        #         print("Invalid Move entered, please enter again!")
        b1.print_ChessBoard()
        eval, b1 = minimax(b1, 3, -math.inf, +math.inf, False, i+1)
        b1.print_ChessBoard()

    print(b1.moves_log)


main()