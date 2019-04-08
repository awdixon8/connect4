class Board():

    def __init__(self):
        self.moves = 0
        self.columns = 7
        self.rows = 6

    def create_board(self):
        self.matrix = [[' ' for y in range(self.columns)] for x in range(self.rows)]

    def get_board(self):
        for row in self.matrix:
            print("|".join(col for col in row))
            # for col in row:
            # print(col, end='|')

    def get_moves(self):
        self.aval_moves = []

    def make_move(self, column):
        self.matrix[0][int(column)] = 'x'
        self.get_moves()

    def is_game_won(self):
        result = False
        x_wins = False
        o_wins = False
        for row in self.matrix:
            if " " in row:
                break
            elif "x" in row:
                if len(set(row)) == 1:
                    x_wins = True
            elif "o" in row:
                if len(set(row)) == 1:
                    o_wins = True
            else:
                print('Draw')
        result = x_wins or o_wins
        print('result is %s' % result)
        return result


def next_turn():
    move = raw_input('Where do you want to move? ')
    board.make_move(move)
    board.get_board()


board = Board()
board.create_board()
board.get_board()
while (not board.is_game_won()) and board.moves <= board.size[0] * board.size[1]:
    next_turn()
