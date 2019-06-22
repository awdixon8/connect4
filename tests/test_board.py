import unittest

from board import Conn4Board


class TestBoardBase(unittest.TestCase):
    def setUp(self):
        self.conn4board = Conn4Board()
        self.conn4board.create_board()

    def tearDown(self):
        pass

    def testCreateBoard(self):
        self.assertEquals(len(self.conn4board.matrix), self.conn4board.rows)
        self.assertEquals(
            len(self.conn4board.matrix[0]), self.conn4board.columns)
        self.conn4board.print_board()
        print(self.conn4board.get_moves())

    def testGetBoard(self):
        rows = 6
        columns = 7
        matrix = [[' ' for y in range(columns)] for x in range(rows)]
        self.assertListEqual(self.conn4board.get_board_state(), matrix)

    def testMakeMove(self):
        self.conn4board.make_move(0)
        self.conn4board.print_board()
        self.assertEquals(
            self.conn4board.get_board_state()[self.conn4board.rows - 1][0],
            'x')
        self.assertEquals(self.conn4board.get_moves()[0],
                          self.conn4board.rows - 2)

    def testMakeBadMove(self):
        self.conn4board.make_move(8)
