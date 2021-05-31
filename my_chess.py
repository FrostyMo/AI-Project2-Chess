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
    def __init__(self, name, position, color, worth,DefendedValue=0,AttackedValue=0):
        self.name = name
        self.position = position
        self.moves = []
        self.color = color
        self.worth = worth
        self.DefendedValue = DefendedValue
        self.AttackedValue = AttackedValue

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

    # def movefrom(self, new_move, BOARD):
    #     # SET THE NEW POSITION OF THIS PIECE TO LATTER HALF OF THE new_move
    #     self.position = new_move[2:]
    #     BOARD[new_move[2:]] = self
    #     # SET THE OLD POSITION OF THIS PIECE TO EMPTY
    #     BOARD[new_move[:2]] = 'E'
    #     return BOARD
def CalculatePieceActionValue( pieceType):

    if  pieceType=='P' or pieceType=='p':
            return 6; 
    elif pieceType=='K' or pieceType=='k':
            return 3
    elif pieceType=='B' or pieceType=='b':
            return 3
    elif pieceType=='R' or pieceType=='r':
            return 2
    elif pieceType=='Q' or pieceType=='q':
            return 1
    elif pieceType=='K' or pieceType=='k':
            return 1
        


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

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board, turn):
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
    def count_attacks(self,moves,board,latest_pos):
        count_attacks=0
        attacked = False
        for move in moves:
            new_position = move[2:]
            old_position = move[:2]
            if board[new_position]!='E':
                count_attacks+=1
            if new_position==latest_pos:
                attacked = True
        return count_attacks,attacked
    def enemy_Attacks(self):
        enemy_moves = self.legal_moves_of(self.board)
        enemy_attacks = []
        count_attacks = 0
        for move in enemy_moves:
            new_position = move[2:]
            old_position = move[:2]
            if self.board[new_position]!='E':
                print("attacked")
                count_attacks+=1
                enemy_attacks.append(move)    

        return enemy_attacks
    def moves_tobe_safe(self):
        lmoves = self.legal_moves(self.board)
        safe_moves = []
        count = 0
        enemy_attacks = self.enemy_Attacks()
        for emoves in enemy_attacks:
            enew_position = emoves[2:]
            eold_position = emoves[:2]
            for moves in lmoves:
                new_position = moves[2:]
                old_position = moves[:2]
                if enew_position==old_position:
                    print("some piece is under attack")
                    self.board[old_position].DefendedValue+=CalculatePieceActionValue(self.board[old_position].name)
                    safe_moves.append(moves)
                    count+=1
        return count, safe_moves
    def moves_to_attack(self):
        legalmoves = self.legal_moves(self.board)
        for moves in legalmoves:
            new_position = moves[2:]
            old_position = moves[:2]
            if self.board[new_position]!='E':
                 self.board[old_position].AttackedValue+=CalculatePieceActionValue(self.board[old_position].name)
    

    # def is_Attacking(self, moves):
    #     board_copy = self.board
    #     count_attacks=0
    #     attackmoves_list = []
    #     new_moves = []
    #     score = 0
    #     for move in moves:
    #         new_position = move[2:]
    #         old_position = move[:2]
    #         if self.board[new_position]!='E':
    #             count_attacks+=1
    #             attackmoves_list.append(move)
    #         temp_piece = board_copy[new_position]
    #         board_copy[new_position] = board_copy[old_position]
    #         board_copy[new_position].position = new_position
    #         board_copy[old_position] = 'E'
    #         new_moves = self.legal_moves_of(board_copy)
    #         num_attacks,is_attacked = self.count_attacks(new_moves,board_copy,new_position)




    def is_CheckMate(self, moves):
        # print(moves)
        board_copy = self.board
        new_moves_list = []
        for move in moves:
            new_position = move[2:]
            old_position = move[:2]

            temp_piece = board_copy[new_position]
            board_copy[new_position] = board_copy[old_position]
            board_copy[new_position].position = new_position
            board_copy[old_position] = 'E'

            if self.is_Check_of(board_copy) != True:
                new_moves_list.append(move)

            board_copy[old_position] = board_copy[new_position]
            board_copy[old_position].position = old_position
            board_copy[new_position] = temp_piece

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

    def move_From(self, new_move):
        # SET THE NEW POSITION OF THIS PIECE TO LATTER HALF OF THE new_move
        new_position = new_move[2:]
        old_position = new_move[:2]
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
        self.is_Check()
        # FLIP TURN
        if self.turn == "White":
            self.turn = "Black"
        else:
            self.turn = "White"
        name = self.board[new_position].name
        self.history[name].append(name + '-' + new_move)

    # Greater the worth of the board, less likely to be selected in minmax
    # So choose minimum worth
    def calculate_Board_Worth(self):
        worth = 0
        # for key in self.board:
        #     if self.board[key] != 'E' and self.board[key].color != self.turn:
        #         worth -= self.board[key].worth
        scoredefend=0
        scoreattack = 0
        for key in self.board:
            if self.board[key] != 'E' and self.board[key].color == self.turn:
                if self.board[key].color == 'White':
                    x, y = index_2d(LIST_BOARD, key)
                    if self.board[key].name.lower() == 'p':
                        worth += self.board[key].worth * PAWN[x][y]
                    elif self.board[key].name.lower() == 'n':
                        worth += self.board[key].worth * KNIGHT[x][y]
                    elif self.board[key].name.lower() == 'b':
                        worth += self.board[key].worth * BISHOP[x][y]
                    elif self.board[key].name.lower() == 'r':
                        worth += self.board[key].worth * ROOK[x][y]
                    elif self.board[key].name.lower() == 'q':
                        worth += self.board[key].worth * QUEEN[x][y]
                    elif self.board[key].name.lower() == 'k':
                        worth += self.board[key].worth * KING[x][y]
                else:
                    x, y = index_2d(LIST_BOARD, key)

                    if self.board[key].name.lower() == 'p':
                        worth += self.board[key].worth * PAWN[7-x][y]
                    elif self.board[key].name.lower() == 'n':
                        worth += self.board[key].worth * KNIGHT[7-x][y]
                    elif self.board[key].name.lower() == 'b':
                        worth += self.board[key].worth * BISHOP[7-x][y]
                    elif self.board[key].name.lower() == 'r':
                        worth += self.board[key].worth * ROOK[7-x][y]
                    elif self.board[key].name.lower() == 'q':
                        worth += self.board[key].worth * QUEEN[7-x][y]
                    elif self.board[key].name.lower() == 'k':
                        worth += self.board[key].worth * KING[7-x][y]

        repititions = len(self.moves_log) - len(set(self.moves_log))
        for move1 in (self.moves_log):
            for move2 in (self.reverse_moves_log):
                if move1 == move2:
                    repititions += 1
        for key in self.board:
            if self.board[key] != 'E':
                scoredefend+=self.board[key].DefendedValue
                scoreattack+= self.board[key].AttackedValue
        
        worth -= repititions * 3
        worth += scoredefend *3
        worth -= scoreattack *3
        return worth

    def push(self, new_move):
        # print("Pushing ", new_move)
        new_position = new_move[2:]
        old_position = new_move[:2]

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

        # print(self.board[self.last_move[-1][:2]].position)
        # print(self.board[self.last_move[-1][2:]])

        self.over_writer.pop()
        self.over_written.pop()
        self.last_move.pop()

        self.moves_log.pop()
        if self.turn == "White":
            self.turn = "Black"
        else:
            self.turn = "White"
