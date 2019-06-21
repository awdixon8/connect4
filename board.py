class Conn4Board(object):
    def __init__(self):
        self.moves = 0
        self.columns = 7
        self.rows = 6
        self.aval_moves = [self.rows - 1 for y in range(self.columns)]

    def create_board(self):
        self.matrix = [[' ' for y in range(self.columns)]
                       for x in range(self.rows)]

    def get_board_state(self):
        return self.matrix

    def print_board(self):
        for row in self.matrix:
            print("|".join(col for col in row))
            # for col in row:
            # print(col, end='|')

    def get_moves(self):
        return self.aval_moves

    def make_move(self, column):
        try:
            if self.aval_moves[column] != '':
                if self.moves % 2 == 0:
                    self.matrix[self.aval_moves[column]][int(column)] = 'x'
                else:
                    self.matrix[self.aval_moves[column]][int(column)] = 'o'
                self.aval_moves[column] = self.aval_moves[column] - 1
                self.moves += 1
            else:
                raise (AssertionError, 'That is not an available move!')
        except IndexError as e:
            print('That is not a valid move.')

    def is_game_won(self):
        result = False
        x_wins = False
        o_wins = False
        for row in self.matrix:
            if self.moves < 7:
                break
            # elif set((x+1)(y)):
            #     break
            # elif set((x)(y+1)):
            #     break
            # elif set((x+1)(y+1)):
            #     break
            # elif set((x-1)(y-1)):
            #     break
            elif row[0] == 'x' and row[0] == 'x' and row[0] == 'x' and row[0] == 'x':
                x_wins = True
        result = x_wins or o_wins
        print('result is %s' % result)
        return result


def next_turn():
    move = raw_input('Where do you want to move? ')
    board.make_move(int(move))
    board.print_board()


board = Conn4Board()
board.create_board()
board.print_board()
while (not board.is_game_won()) and board.moves <= board.columns * board.rows:
    next_turn()
