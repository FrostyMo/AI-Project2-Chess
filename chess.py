print("hi")


def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))


class Player:
    def __init__(self, name, position, color):
        self.name = name
        self.position = position
        self.moves = []
        self.color = color

    def __str__(self):
        return self.name

    def get_Name(self):
        print("I am a ", self.name)
        return self.name

    def get_Position(self):
        print("I am at: ", self.position)
        return self.position

    def moves_Available(self, list_board, board):
        print("Im just a nameless player")


class Pawn(Player):

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board):
        self.moves.clear()
        i, j = index_2d(list_board, self.position)

        if self.color == "Black":
            if '7' in self.position:
                if board[list_board[i+1][j]] == 'Empty':
                    self.moves.append(list_board[i+1][j])
                    if board[list_board[i+2][j]] == 'Empty':
                        self.moves.append(list_board[i+2][j])
            else:
                if board[list_board[i+1][j]] == 'Empty':
                    self.moves.append(list_board[i+1][j])

            # If not right most
            if (j != 7):
                # If the diagonal has an ENEMY piece
                if board[list_board[i+1][j+1]] != 'Empty':
                    if board[list_board[i+1][j+1]].color == "White":
                        self.moves.append(list_board[i+1][j+1])

            # If not left most
            if (j != 0):
                # If the diagonal has an ENEMY piece
                if board[list_board[i+1][j-1]] != 'Empty':
                    if board[list_board[i+1][j-1]].color == "White":
                        self.moves.append(list_board[i+1][j-1])

        else:
            if '2' in self.position:
                if board[list_board[i-1][j]] == 'Empty':
                    self.moves.append(list_board[i-1][j])
                    if board[list_board[i-2][j]] == 'Empty':
                        self.moves.append(list_board[i-2][j])
            else:
                if board[list_board[i-1][j]] == 'Empty':
                    self.moves.append(list_board[i-1][j])

            # If not right most
            if (j != 7):
                # If the diagonal has an ENEMY piece
                if board[list_board[i-1][j+1]] != 'Empty':
                    if board[list_board[i-1][j+1]].color == "Black":
                        self.moves.append(list_board[i-1][j+1])

            # If not left most
            if (j != 0):
                # If the diagonal has an ENEMY piece
                if board[list_board[i-1][j-1]] != 'Empty':
                    if board[list_board[i-1][j-1]].color == "Black":
                        self.moves.append(list_board[i-1][j-1])


class Knight(Player):

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board):
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
                if board[list_board[x][y]] != 'Empty':
                    print(board[list_board[x][y]])
                    if board[list_board[x][y]].color != self.color:
                        self.moves.append(list_board[x][y])
                    break
                else:
                    self.moves.append(list_board[x][y])


class Bishop(Player):

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board):
        self.moves.clear()
        x, y = index_2d(list_board, self.position)

        def Append(dx, dy):
            for i in range(1, 8):
                newx = x + dx*i
                newy = y + dy*i

                if 0 <= newx < 8 and 0 <= newy < 8:
                    if board[list_board[newx][newy]] != 'Empty':
                        print(board[list_board[newx][newy]])
                        if board[list_board[newx][newy]].color != self.color:
                            self.moves.append(list_board[newx][newy])
                            break
                        break
                    else:
                        self.moves.append(list_board[newx][newy])
                else:
                    break

        for dx in (-1, 1):
            for dy in (-1, 1):
                Append(dx, dy)


class Rook(Player):

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board):
        self.moves.clear()
        x, y = index_2d(list_board, self.position)

        def Append(dx, dy):
            for i in range(1, 8):
                newx = x + dx*i
                newy = y + dy*i

                if 0 <= newx < 8 and 0 <= newy < 8:
                    if board[list_board[newx][newy]] != 'Empty':
                        print(board[list_board[newx][newy]])
                        if board[list_board[newx][newy]].color != self.color:
                            self.moves.append(list_board[newx][newy])
                            break
                        break
                    else:
                        self.moves.append(list_board[newx][newy])
                else:
                    break

        Append(0, 1)
        Append(0, -1)
        Append(1, 0)
        Append(-1, 0)


class Queen(Player):

    def __str__(self):
        return self.name

    def moves_Available(self, list_board, board):
        self.moves.clear()
        x, y = index_2d(list_board, self.position)

        def Append(dx, dy):
            for i in range(1, 8):
                newx = x + dx*i
                newy = y + dy*i

                if 0 <= newx < 8 and 0 <= newy < 8:
                    if board[list_board[newx][newy]] != 'Empty':
                        print(board[list_board[newx][newy]])
                        if board[list_board[newx][newy]].color != self.color:
                            self.moves.append(list_board[newx][newy])
                            break
                        break
                    else:
                        self.moves.append(list_board[newx][newy])
                else:
                    break

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    pass
                else:
                    Append(dx, dy)
