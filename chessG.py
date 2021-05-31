import chess
import chess.svg
import time
from random import randint
from IPython.display import display, Image
board = chess.Board()

print(board.legal_moves)
# chess.svg.piece(chess.Piece.from_symbol("R"))
while(True):
    legal_moves = list(board.legal_moves)
    print(legal_moves)
    move = chess.Move.from_uci(
        str(legal_moves[randint(0, len(legal_moves)-1)]))
    board.push(move)

    time.sleep(1)
    display(board)
