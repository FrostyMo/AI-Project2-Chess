from static_values import *

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


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


class Player:

    def __init__(self, name, position, color, worth, DefendedValue=0, AttackedValue=0):

        self.name = name
        self.position = position
        self.moves = []
        self.color = color
        self.worth = worth
        self.has_moved = False
        self.DefendedValue = 0
        self.AttackedValue = 0

    def __str__(self):
        return self.name

    def get_Name(self):
        print("I am a ", self.name)
        return self.name

    def get_Position(self):
        print("I am at: ", self.position)
        return self.position

    def moves_Available(self, list_board, board, turn):
        print("Im just a nameless player")


class Pawn(Player):

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board, turn):
        self.moves.clear()
        i, j = index_2d(list_board, self.position)

        if self.color == "Black" and turn == "Black":
            if '7' in self.position:
                if board[list_board[i+1][j]] == 'E':
                    self.moves.append(self.position+list_board[i+1][j])
                    if board[list_board[i+2][j]] == 'E':
                        self.moves.append(self.position+list_board[i+2][j])
            else:
                if board[list_board[i+1][j]] == 'E':
                    self.moves.append(self.position+list_board[i+1][j])

            # If not right most
            if (j != 7):
                # If the diagonal has an ENEMY piece
                if board[list_board[i+1][j+1]] != 'E':
                    if board[list_board[i+1][j+1]].color == "White":
                        self.moves.append(self.position+list_board[i+1][j+1])

            # If not left most
            if (j != 0):
                # If the diagonal has an ENEMY piece
                if board[list_board[i+1][j-1]] != 'E':
                    if board[list_board[i+1][j-1]].color == "White":
                        self.moves.append(self.position+list_board[i+1][j-1])

        elif self.color == "White" and turn == "White":
            if '2' in self.position:
                if board[list_board[i-1][j]] == 'E':
                    self.moves.append(self.position+list_board[i-1][j])
                    if board[list_board[i-2][j]] == 'E':
                        self.moves.append(self.position+list_board[i-2][j])
            else:
                if board[list_board[i-1][j]] == 'E':
                    self.moves.append(self.position+list_board[i-1][j])

            # If not right most
            if (j != 7):
                # If the diagonal has an ENEMY piece
                if board[list_board[i-1][j+1]] != 'E':
                    if board[list_board[i-1][j+1]].color == "Black":
                        self.moves.append(self.position+list_board[i-1][j+1])

            # If not left most
            if (j != 0):
                # If the diagonal has an ENEMY piece
                if board[list_board[i-1][j-1]] != 'E':
                    if board[list_board[i-1][j-1]].color == "Black":
                        self.moves.append(self.position+list_board[i-1][j-1])


class Knight(Player):

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board, turn):
        # if self.color == turn:
        self.moves.clear()
        i, j = index_2d(list_board, self.position)

        X = [2, 1, -1, -2, -2, -1, 1, 2]
        Y = [1, 2, 2, 1, -1, -2, -2, -1]

        # Check if each possible move
        # is valid or not
        for a in range(8):

            # Position of knight after move
            x = i + X[a]
            y = j + Y[a]

            # count valid moves
            if x >= 0 and y >= 0 and x < 8 and y < 8:
                if board[list_board[x][y]] != 'E':
                    # print(board[list_board[x][y]])
                    if board[list_board[x][y]].color != self.color:
                        # print(x, y)
                        self.moves.append(self.position+list_board[x][y])
                else:
                    self.moves.append(self.position+list_board[x][y])


class Bishop(Player):

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board, turn):
        # if self.color == turn:
        self.moves.clear()
        x, y = index_2d(list_board, self.position)

        def Append(dx, dy):
            for i in range(1, 8):
                newx = x + dx*i
                newy = y + dy*i

                if 0 <= newx < 8 and 0 <= newy < 8:
                    if board[list_board[newx][newy]] != 'E':
                        # print(board[list_board[newx][newy]])
                        if board[list_board[newx][newy]].color != self.color:
                            self.moves.append(
                                self.position+list_board[newx][newy])
                            break
                        break
                    else:
                        self.moves.append(
                            self.position+list_board[newx][newy])
                else:
                    break

        for dx in (-1, 1):
            for dy in (-1, 1):
                Append(dx, dy)


class Rook(Player):

    # def __init__(self, has_moved=False):
    #     self.has_moved = has_moved

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board, turn):
        # if self.color == turn:
        self.moves.clear()
        x, y = index_2d(list_board, self.position)

        def Append(dx, dy):
            for i in range(1, 8):
                newx = x + dx*i
                newy = y + dy*i

                if 0 <= newx < 8 and 0 <= newy < 8:
                    if board[list_board[newx][newy]] != 'E':
                        # print(board[list_board[newx][newy]])
                        if board[list_board[newx][newy]].color != self.color:
                            self.moves.append(
                                self.position+list_board[newx][newy])
                            break
                        break
                    else:
                        self.moves.append(
                            self.position+list_board[newx][newy])
                else:
                    break

        Append(0, 1)
        Append(0, -1)
        Append(1, 0)
        Append(-1, 0)


class Queen(Player):

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board, turn):
        # if self.color == turn:

        self.moves.clear()
        x, y = index_2d(list_board, self.position)

        def Append(dx, dy):
            for i in range(1, 8):
                newx = x + dx*i
                newy = y + dy*i

                if 0 <= newx < 8 and 0 <= newy < 8:
                    if board[list_board[newx][newy]] != 'E':
                        # print(board[list_board[newx][newy]])
                        if board[list_board[newx][newy]].color != self.color:
                            self.moves.append(
                                self.position+list_board[newx][newy])
                            break
                        break
                    else:
                        self.moves.append(
                            self.position+list_board[newx][newy])
                else:
                    break

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    pass
                else:
                    Append(dx, dy)


class King(Player):

    # def __init__(self, has_moved=False):
    #     self.has_moved = has_moved

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board, turn):
        if self.position not in ['e1', 'e8']:
            self.has_moved = True
       # if self.color == turn:
        self.moves.clear()
        x, y = index_2d(list_board, self.position)

        def Append(dx, dy):

            newx = x + dx
            newy = y + dy

            if 0 <= newx < 8 and 0 <= newy < 8:
                if board[list_board[newx][newy]] != 'E':
                    # print(board[list_board[newx][newy]])
                    if board[list_board[newx][newy]].color != self.color:

                        self.moves.append(
                            self.position+list_board[newx][newy])

                else:
                    self.moves.append(self.position+list_board[newx][newy])

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    pass
                else:
                    Append(dx, dy)

        if self.has_moved == False:
            if self.color == 'White':
                rook1 = list_board[7][0]
                rook2 = list_board[7][7]
                if board[rook1] != 'E':
                    if board[rook1].name == 'r':
                        if board[rook1].has_moved == False:
                            can_castle = True
                            for i in range(1, 4):
                                if board[list_board[7][y-i]] != 'E':
                                    can_castle = False
                            if can_castle:
                                self.moves.append("e1c1")
                if board[rook2] != 'E':
                    # print("Rook 2 found at ", rook2)
                    if board[rook2].name == 'r':
                        # print("r found")
                        if board[rook2].has_moved == False:
                            # print("Rook 2 hasnt moved")
                            can_castle = True
                            # print("y: ", y, end="  ")
                            for i in range(1, 3):
                                # print("Checking: ", list_board[7][y+i])
                                if board[list_board[7][y+i]] != 'E':
                                    can_castle = False
                            if can_castle:
                                self.moves.append("e1g1")

            else:
                rook1 = list_board[0][0]
                rook2 = list_board[0][7]
                if board[rook1] != 'E':
                    if board[rook1].name == 'R':
                        if board[rook1].has_moved == False:
                            can_castle = True
                            for i in range(1, 4):
                                if board[list_board[0][y-i]] != 'E':
                                    can_castle = False
                            if can_castle:
                                self.moves.append("e8c8")
                if board[rook2] != 'E':
                    if board[rook2].name == 'R':
                        if board[rook2].has_moved == False:
                            can_castle = True
                            for i in range(1, 3):
                                if board[list_board[0][y+i]] != 'E':
                                    can_castle = False
                            if can_castle:
                                self.moves.append("e8g8")


class Board:

    def __init__(self, player="White", AI="Black"):
        self.player = player
        self.AI = AI
        self.turn = "White"
        self.board = {}
        self.check = False
        self.check_Mate = False
        self.create_Board()
        self.history = {'R': [], 'r': [], 'N': [], 'n': [], 'B': [], 'b': [
        ], 'Q': [], 'q': [], 'K': [], 'k': [], 'P': [], 'p': []}
        self.over_written = []
        self.over_writer = []
        self.last_move = []
        self.moves_log = []
        self.reverse_moves_log = []
        self.pawn_worth = 100
        self.knight_worth = 320
        self.bishop_worth = 330
        self.rook_worth = 500
        self.queen_worth = 900
        self.king_worth = 10000
        self.stale_mate = False
        self.named_move = []

    def legal_moves_of(self, board):
        global LIST_BOARD
        moves_list = []

        for key in board:
            if board[key] != 'E' and self.turn != board[key].color:
                # print(BOARD[key].position)
                board[key].moves_Available(
                    LIST_BOARD, board, board[key].color)
                moves = board[key].moves
                if (len(moves) > 0):
                    moves_list.append(moves)
        x = [j for sub in moves_list for j in sub]

        return x

    def legal_moves(self):
        global LIST_BOARD
        moves_list = []

        for key in self.board:
            if self.board[key] != 'E' and self.turn == self.board[key].color:
                # print(BOARD[key].position)
                self.board[key].moves_Available(
                    LIST_BOARD, self.board, self.turn)
                moves = self.board[key].moves
                if (len(moves) > 0):
                    moves_list.append(moves)
        x = [j for sub in moves_list for j in sub]

        # if self.check is True:

        y = self.is_CheckMate(x)
        if len(y) == 0:
            self.check_Mate = True
        # self.check = False
        s = self.is_Stalemate(y)
        if s == True:
            self.stale_mate = True
            print("It's a draw!")
        return y

        # return x

    def create_Board(self):
        global BOARD
        global TWO_BOARD
        global LIST_BOARD

        a = ord('a')
        n = ord('8')
        alph = [chr(i) for i in range(a, a+8)]
        numbers = [chr(i) for i in range(n, n-8, -1)]

        for i_index, i in enumerate(numbers):
            mylist = []
            for j_index, j in enumerate(alph):
                if (TWO_BOARD[i_index][j_index] == 0):
                    BOARD[j+i] = "E"
                elif (TWO_BOARD[i_index][j_index] == 1):
                    if (i == '8'):
                        BOARD[j+i] = King("K", j+i, "Black", 10000)
                    else:
                        BOARD[j+i] = King("k", j+i, "White", 10000)
                elif (TWO_BOARD[i_index][j_index] == 2):
                    if (i == '8'):
                        BOARD[j+i] = Queen("Q", j+i, "Black", 9)
                    else:
                        BOARD[j+i] = Queen("q", j+i, "White", 9)
                elif (TWO_BOARD[i_index][j_index] == 3):
                    if (i == '8'):
                        BOARD[j+i] = Knight("N", j+i, "Black", 3)
                    else:
                        BOARD[j+i] = Knight("n", j+i, "White", 3)
                elif (TWO_BOARD[i_index][j_index] == 4):

                    if (i == '8'):
                        BOARD[j+i] = Bishop("B", j+i, "Black", 3)
                    else:
                        BOARD[j+i] = Bishop("b", j+i, "White", 3)
                elif (TWO_BOARD[i_index][j_index] == 5):
                    if (i == '8'):
                        BOARD[j+i] = Rook("R", j+i, "Black", 5)
                    else:
                        BOARD[j+i] = Rook("r", j+i, "White", 5)
                elif (TWO_BOARD[i_index][j_index] == 6):
                    if (i == '7'):
                        BOARD[j+i] = Pawn("P", j+i, "Black", 1)
                    else:
                        BOARD[j+i] = Pawn("p", j+i, "White", 1)
                mylist.append(j+i)
            LIST_BOARD.append(mylist)
    # print_Board()
        self.board = BOARD
        self.print_ChessBoard()

    def print_ChessBoard(self):

        print("\n\n~~~~~ {}'s TURN ~~~~~\n".format(self.turn))

        print("    ", end=" ")
        for i in range(ord('a'), ord('a')+8):
            print(chr(i), end=" ")
        print("\n")

        for i, key in enumerate(self.board):
            if (i) % 8 == 0:
                print("{} | ".format(key[1]), self.board[key], end=" ")
            else:
                print(self.board[key], end=" ")

            if (i+1) % 8 == 0 and i != 0:
                print(" | {}".format(key[1]))

        print("\n    ", end=" ")
        for i in range(ord('a'), ord('a')+8):
            print(chr(i), end=" ")
        print("\n")

    def print_Board(self):
        for i, key in enumerate(self.board):
            print("['{}': ".format(key), self.board[key], end="] ")
            if (i+1) % 8 == 0 and i != 0:
                print("")

    def promote(self, new_position):
        promotion = ''
        while True:
            if self.board[new_position].name == 'P':
                promotion = input(
                    "Please enter the promotion name for the Pawn: (R, N, Q, B)")
                if promotion in ['R', 'N', 'Q', 'B']:
                    break
            else:
                promotion = input(
                    "Please enter the promotion name for the Pawn: (r, n, q, b)")
                if promotion in ['r', 'n', 'q', 'b']:
                    break

        if promotion in ['R', 'r']:
            self.board[new_position] = Rook(
                promotion, new_position, self.turn, 5)
        elif promotion in ['N', 'n']:
            self.board[new_position] = Knight(
                promotion, new_position, self.turn, 3)
        elif promotion in ['Q', 'q']:
            self.board[new_position] = Queen(
                promotion, new_position, self.turn, 9)
        elif promotion in ['B', 'b']:
            self.board[new_position] = Bishop(
                promotion, new_position, self.turn, 3)

    def CalculatePieceActionValue(self, pieceType):
        if pieceType == 'P' or pieceType == 'p':
            return 6
        elif pieceType == 'N' or pieceType == 'n':
            return 3
        elif pieceType == 'B' or pieceType == 'b':
            return 3
        elif pieceType == 'R' or pieceType == 'r':
            return 2
        elif pieceType == 'Q' or pieceType == 'q':
            return 1
        elif pieceType == 'K' or pieceType == 'k':
            return 1

    def count_attacks(self, moves, board, latest_pos):
        count_attacks = 0
        attacked = False
        for move in moves:
            new_position = move[2:]
            old_position = move[:2]
            if board[new_position] != 'E':
                count_attacks += 1
            if new_position == latest_pos:
                attacked = True
        return count_attacks, attacked

    def enemy_Attacks(self, board):
        enemy_moves = self.legal_moves_of(board)
        enemy_attacks = []
        count_attacks = 0
        for move in enemy_moves:
            new_position = move[2:]
            old_position = move[:2]
            if board[new_position] != 'E':
                count_attacks += 1
                enemy_attacks.append(move)

        return enemy_attacks, count_attacks

    def moves_to_be_safe(self):
        lmoves = self.legal_moves()
        safe_moves = []
        count = 0
        enemy_attacks, ecount = self.enemy_Attacks(self.board)
        for emoves in enemy_attacks:
            enew_position = emoves[2:]
            eold_position = emoves[:2]
            for moves in lmoves:
                new_position = moves[2:]
                old_position = moves[:2]
                if enew_position == old_position:

                    if self.board[old_position] != 'E':
                        # print("some piece is under attack")
                        # print("NAME ",self.board[old_position].name)
                        self.board[old_position].DefendedValue += self.CalculatePieceActionValue(
                            self.board[old_position].name)
                        safe_moves.append(moves)
                        count += 1
        return count, safe_moves

    def moves_to_attack(self):
        legalmoves = self.legal_moves()
        for moves in legalmoves:
            new_position = moves[2:]
            old_position = moves[:2]
            if self.board[new_position] != 'E':
                self.board[old_position].AttackedValue += self.CalculatePieceActionValue(
                    self.board[old_position].name)

    def Defending_pieces(self):
        board_copy = self.board
        legalmoves = self.legal_moves()
        enemy_attacks, ecount = self.enemy_Attacks(self.board)
        for move in legalmoves:
            new_position = move[2:]
            old_position = move[:2]
            if self.board[old_position].name in ['k', 'K']:
                self.board[old_position].has_moved = True
            temp_piece = self.board[new_position]
            self.board[new_position] = self.board[old_position]
            self.board[new_position].position = new_position
            self.board[old_position] = 'E'
            enemy_attacks2, ecount2 = self.enemy_Attacks(self.board)
            if ecount2 < ecount:
                if self.board[new_position] != 'E':
                    self.board[new_position].DefendedValue += self.CalculatePieceActionValue(
                        self.board[new_position].name)
            self.board[old_position] = self.board[new_position]
            self.board[old_position].position = old_position
            self.board[new_position] = temp_piece
            if self.board[old_position].name in ['k', 'K']:
                self.board[old_position].has_moved = False

    def is_CheckMate(self, moves):
        # print(moves)
        board_copy = self.board
        new_moves_list = []
        for move in moves:
            new_position = move[2:]
            old_position = move[:2]
            if self.board[old_position].name in ['k', 'K']:
                self.board[old_position].has_moved = True
            temp_piece = board_copy[new_position]
            board_copy[new_position] = board_copy[old_position]
            board_copy[new_position].position = new_position
            board_copy[old_position] = 'E'

            if self.is_Check_of(board_copy) != True:
                new_moves_list.append(move)

            board_copy[old_position] = board_copy[new_position]
            board_copy[old_position].position = old_position
            board_copy[new_position] = temp_piece
            if self.board[old_position].name in ['k', 'K']:
                self.board[old_position].has_moved = False
        return new_moves_list

    def is_Check_of(self, board):
        moves = self.legal_moves_of(board)
        king_position = ''

        # Check danger on a white king, given turn for a black piece and vice versa
        for key in board:
            if board[key] != 'E':
                if (board[key].name == 'k' and self.turn == 'White') or (board[key].name == 'K' and self.turn == 'Black'):
                    king_position = board[key].position

        # If any new position in legal moves targetting the King, it's a check
        for move in moves:
            if king_position == move[2:]:
                return True
        return False

    def is_Check(self):
        moves = self.legal_moves()
        king_position = ''

        # Check danger on a white king, given turn for a black piece and vice versa
        for key in self.board:
            if self.board[key] != 'E':
                if (self.board[key].name == 'k' and self.turn == 'Black') or (self.board[key].name == 'K' and self.turn == 'White'):
                    king_position = self.board[key].position

        # If any new position in legal moves targetting the King, it's a check
        for move in moves:
            if king_position == move[2:]:
                self.check = True

    def is_Stalemate(self, moves):
        if self.is_Check_of(self.board) == False:
            if(len(moves) == 0):
                return True
        return False

    def move_From(self, new_move):

        # SET THE NEW POSITION OF THIS PIECE TO LATTER HALF OF THE new_move
        new_position = new_move[2:]
        old_position = new_move[:2]

        castle_bool = False
        if new_move in ['e1g1', 'e8g8', 'e1c1', 'e8c8']:
            if self.board[old_position].name in ['k', 'K']:
                self.board[old_position].has_moved = True
                self.castle(new_move)
                castle_bool = True

        if castle_bool == False:
            if (self.board[new_position] != 'E' and self.board[new_position].name in ['k', 'K']):
                print("AAAAAAA YOU ARE WRONG")
                self.check_Mate = True
                return
            self.board[new_position] = self.board[old_position]
            self.board[new_position].position = new_position

            if '1' in new_position and self.board[new_position].name == 'P':
                self.promote(new_position)
            elif '8' in new_position and self.board[new_position].name == 'p':
                self.promote(new_position)

            # SET THE OLD POSITION OF THIS PIECE TO EMPTY
            self.board[old_position] = 'E'
            # self.is_Check()
            # FLIP TURN
            if self.turn == "White":
                self.turn = "Black"
            else:
                self.turn = "White"
            name = self.board[new_position].name
            self.history[name].append(name + '-' + new_move)
            self.named_move.append(name+'-'+new_move)

    def material_Worth(self):
        bp = wp = bb = wb = bn = wn = bq = wq = br = wr = bk = wk = 0
        for key in self.board:
            if self.board[key] != 'E':
                if self.board[key].name == 'p':
                    wp += 1
                elif self.board[key].name == 'P':
                    bp += 1
                elif self.board[key].name == 'b':
                    wb += 1
                elif self.board[key].name == 'B':
                    bb += 1
                elif self.board[key].name == 'n':
                    wn += 1
                elif self.board[key].name == 'N':
                    bn += 1
                elif self.board[key].name == 'q':
                    wq += 1
                elif self.board[key].name == 'Q':
                    bq += 1
                elif self.board[key].name == 'r':
                    wr += 1
                elif self.board[key].name == 'R':
                    br += 1
                elif self.board[key].name == 'k':
                    wp += 1
                elif self.board[key].name == 'K':
                    bp += 1
        material_worth = self.pawn_worth * (wp-bp)
        material_worth += self.knight_worth * (wn-bn)
        material_worth += self.bishop_worth * (wb-bb)
        material_worth += self.rook_worth * (wr-br)
        material_worth += self.queen_worth * (wq-bq)
        material_worth += self.king_worth * (wk-bk)

        return material_worth

    def individual_Worth(self):
        worth = 0
        for key in self.board:
            if self.board[key] != 'E':
                if self.board[key].color == 'White':
                    x, y = index_2d(LIST_BOARD, key)
                    if self.board[key].name.lower() == 'p':
                        worth += PAWN[x][y]
                    elif self.board[key].name.lower() == 'n':
                        worth += KNIGHT[x][y]
                    elif self.board[key].name.lower() == 'b':
                        worth += BISHOP[x][y]
                    elif self.board[key].name.lower() == 'r':
                        worth += ROOK[x][y]
                    elif self.board[key].name.lower() == 'q':
                        worth += QUEEN[x][y]
                    elif self.board[key].name.lower() == 'k':
                        worth += KING[x][y]
                else:
                    x, y = index_2d(LIST_BOARD, key)

                    if self.board[key].name.lower() == 'p':
                        worth += (- PAWN[7-x][y])
                    elif self.board[key].name.lower() == 'n':
                        worth += (- KNIGHT[7-x][y])
                    elif self.board[key].name.lower() == 'b':
                        worth += (- BISHOP[7-x][y])
                    elif self.board[key].name.lower() == 'r':
                        worth += (- ROOK[7-x][y])
                    elif self.board[key].name.lower() == 'q':
                        worth += (- QUEEN[7-x][y])
                    elif self.board[key].name.lower() == 'k':
                        worth += (- KING[7-x][y])
        return worth

    # Greater the worth of the board, less likely to be selected in minmax
    # So choose minimum worth

    def calculate_Board_Worth(self):
        worth = 0
        # for key in self.board:
        #     if self.board[key] != 'E' and self.board[key].color != self.turn:
        #         worth -= self.board[key].worth
        material_worth = self.material_Worth()

        scoredefend = 0
        scoreattack = 0

        # for key in self.board:
        #     if self.board[key] != 'E' and self.board[key].color == self.turn:
        #         if self.board[key].color == 'White':
        #             x, y = index_2d(LIST_BOARD, key)
        #             if self.board[key].name.lower() == 'p':
        #                 worth += self.board[key].worth * PAWN[x][y]
        #             elif self.board[key].name.lower() == 'n':
        #                 worth += self.board[key].worth * KNIGHT[x][y]
        #             elif self.board[key].name.lower() == 'b':
        #                 worth += self.board[key].worth * BISHOP[x][y]
        #             elif self.board[key].name.lower() == 'r':
        #                 worth += self.board[key].worth * ROOK[x][y]
        #             elif self.board[key].name.lower() == 'q':
        #                 worth += self.board[key].worth * QUEEN[x][y]
        #             elif self.board[key].name.lower() == 'k':
        #                 worth += self.board[key].worth * KING[x][y]
        #         else:
        #             x, y = index_2d(LIST_BOARD, key)

        #             if self.board[key].name.lower() == 'p':
        #                 worth += self.board[key].worth * (- PAWN[7-x][y])
        #             elif self.board[key].name.lower() == 'n':
        #                 worth += self.board[key].worth * (- KNIGHT[7-x][y])
        #             elif self.board[key].name.lower() == 'b':
        #                 worth += self.board[key].worth * (- BISHOP[7-x][y])
        #             elif self.board[key].name.lower() == 'r':
        #                 worth += self.board[key].worth * (- ROOK[7-x][y])
        #             elif self.board[key].name.lower() == 'q':
        #                 worth += self.board[key].worth * (- QUEEN[7-x][y])
        #             elif self.board[key].name.lower() == 'k':
        #                 worth += self.board[key].worth * (- KING[7-x][y])
        indv_worth = self.individual_Worth()
        worth += indv_worth
        worth += material_worth
        repititions = len(self.moves_log) - len(set(self.moves_log))
        for move1 in (self.moves_log):
            for move2 in (self.reverse_moves_log):
                if move1 == move2:
                    repititions += 1

        safe_moves = []
        # self.moves_to_attack()
        # count, safe_moves = self.moves_to_be_safe()
        # self.Defending_pieces()
        # for key in self.board:
        #     if self.board[key] != 'E':
        #         scoredefend += self.board[key].DefendedValue
        #         scoreattack += self.board[key].AttackedValue

        worth -= repititions * 4

        #worth += scoredefend
        #worth += scoreattack

        if self.turn == "Black":
            worth *= -1
        return worth

    def is_capture(self, new_move):
        new_position = new_move[2:]

        if self.board[new_position] != 'E':
            return True
        return False

    def castle(self, new_move):
        xK, yK = index_2d(LIST_BOARD, new_move[:2])
        if new_move in ['e1g1', 'e8g8']:
            old_position = new_move[:2]
            new_position = new_move[2:]
            self.board[new_position] = self.board[old_position]
            self.board[new_position].position = new_position
            self.board[old_position] = 'E'

            # King moved
            name = self.board[new_position].name
            self.history[name].append(name + '-' + new_move)

            rook_position = 'h' + old_position[1]

            rook_newposition = LIST_BOARD[xK][yK+1]

            self.board[rook_newposition] = self.board[rook_position]
            self.board[rook_newposition].position = rook_newposition
            self.board[rook_position] = 'E'

            # Rook moved
            name = self.board[rook_newposition].name
            self.history[name].append(
                name + '-' + rook_position+rook_newposition)

            if self.turn == "White":
                self.turn = "Black"
            else:
                self.turn = "White"
        elif new_move in ['e1c1', 'e8c8']:
            old_position = new_move[:2]
            new_position = new_move[2:]
            self.board[new_position] = self.board[old_position]
            self.board[new_position].position = new_position
            self.board[old_position] = 'E'

            # King moved
            name = self.board[new_position].name
            self.history[name].append(name + '-' + new_move)

            rook_position = 'h' + old_position[1]
            rook_newposition = LIST_BOARD[xK][yK-1]

            self.board[rook_newposition] = self.board[rook_position]
            self.board[rook_newposition].position = rook_newposition
            self.board[rook_position] = 'E'

            # Rook moved
            name = self.board[rook_newposition].name
            self.history[name].append(
                name + '-' + rook_position+rook_newposition)

            if self.turn == "White":
                self.turn = "Black"
            else:
                self.turn = "White"

    def push(self, new_move):
        # print("Pushing ", new_move)
        new_position = new_move[2:]
        old_position = new_move[:2]
        if self.board[old_position].name in ['k', 'K']:
            self.board[old_position].has_moved = True

        # Save the overwritten and overwrite pieces for pop
        self.over_written.append(self.board[new_position])
        self.over_writer.append(self.board[old_position])
        self.last_move.append(new_move)

        self.board[new_position] = self.board[old_position]
        self.board[new_position].position = new_position
        if '1' in new_position and self.board[new_position].name == 'P':
            self.board[new_position] = Queen(
                'Q', new_position, self.turn, 9)
        elif '8' in new_position and self.board[new_position].name == 'p':
            self.board[new_position] = Queen(
                'q', new_position, self.turn, 9)

        # SET THE OLD POSITION OF THIS PIECE TO EMPTY
        self.board[old_position] = 'E'
        if self.turn == "White":
            self.turn = "Black"
        else:
            self.turn = "White"

        name = self.board[new_position].name
        # self.history[name].append(name + '-' + new_move)
        self.moves_log.append(new_move)
        self.reverse_moves_log.append(new_move[2:] + new_move[:2])

    def pop(self):
        # print("Popping ", self.last_move[-1])

        # print(self.board[self.last_move[-1][:2]])
        # print(self.board[self.last_move[-1][2:]].position)
        self.board[self.last_move[-1][:2]] = self.over_writer[-1]
        self.board[self.last_move[-1][2:]] = self.over_written[-1]
        self.board[self.last_move[-1][:2]].position = self.last_move[-1][:2]
        if self.board[self.last_move[-1][2:]] != 'E':
            self.board[self.last_move[-1][2:]
                       ].position = self.last_move[-1][2:]

        if self.board[self.last_move[-1][:2]].name in ['k', 'K']:
            self.board[self.last_move[-1][:2]].has_moved = False
        # print(self.board[self.last_move[-1][:2]].position)
        # print(self.board[self.last_move[-1][2:]])

        self.over_writer.pop()
        self.over_written.pop()
        self.last_move.pop()
        self.check_Mate = False
        self.check_Mate = False
        self.moves_log.pop()
        if self.turn == "White":
            self.turn = "Black"
        else:
            self.turn = "White"
