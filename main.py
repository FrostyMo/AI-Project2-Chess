from my_chess import *
from random import randint
from copy import deepcopy
import math

CHESS_BOARD = None


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


def quiesce(alpha, beta):
    stand_pat = CHESS_BOARD.calculate_Board_Worth()
    if (stand_pat >= beta):
        return beta
    if (alpha < stand_pat):
        alpha = stand_pat
    for move in CHESS_BOARD.legal_moves():
        if CHESS_BOARD.is_capture(move):
            CHESS_BOARD.push(move)
            score = -quiesce(-beta, -alpha)
            CHESS_BOARD.pop()
            if (score >= beta):
                return beta
            if (score > alpha):
                alpha = score
    return alpha


def minimax2(depth, alpha, beta):

    bestscore = -9999
    if depth == 0:  # or game over
        # Static eval of position
        return CHESS_BOARD.calculate_Board_Worth(), None

    moves = CHESS_BOARD.legal_moves()
    maxEval = -math.inf
    best_move = None
    for move in moves:
        CHESS_BOARD.push(move)
        eval, any_move = minimax2(depth-1, alpha, beta)
        CHESS_BOARD.pop()

        eval *= -1
        if (eval >= beta):
            return eval, best_move
        if (eval > bestscore):
            bestscore = eval
            best_move = move
        if (eval > alpha):
            alpha = eval

    return bestscore, best_move


def main():
    b = Board()

    board_copy = b
    b1 = board_copy
    global CHESS_BOARD
    CHESS_BOARD = b1

    for i in range(100):
        # eval, b1 = minimax(b1, 2, -math.inf, +math.inf, True, i+1)
        # board_copy.print_ChessBoard()
        b1.print_ChessBoard()
        if b1.stale_mate == True:
            print("\nStalemate!\n")
            break
        if b1.check_Mate == True:
            print("\Check Mate!\n")
            break
        moves = b1.legal_moves()
        if b1.check_Mate == True or len(moves) == 0:
            print("\Check Mate!\n")
            break
        eval, move = minimax2(2, -math.inf, +math.inf)
        b1.move_From(move)
        print(moves)
        # while True:
        #     new_move = input("Please enter your move (e.g a2a4): ")
        #     if new_move in moves:
        #         b1.move_From(new_move)
        #         break
        #     else:
        #         print("Invalid Move entered, please enter again!")
        print("PLAYER MOVED: ", b1.named_move[-1])
        b1.print_ChessBoard()

        if b1.stale_mate == True:
            print("\nStalemate!\n")
            break
        elif b1.check_Mate == True:
            print("\Check Mate!\n")
            break
        CHESS_BOARD = b1
        eval, move = minimax2(2, -math.inf, +math.inf)
        if b1.stale_mate == True:
            print("\nStalemate!\n")
            break
        elif b1.check_Mate == True:
            print("\nCheck Mate!\n")
            break
        b1.move_From(move)
        print("AI MOVED: ", b1.named_move[-1])
        CHESS_BOARD = b1
        # b1.print_ChessBoard()

    # b1.print_ChessBoard()
    # m=b.CalculatePieceActionValue('P')
    # print(m)
    print(b1.moves_log)


main()
