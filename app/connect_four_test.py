import unittest


from connect_four import init, fillBoard, player2, player1,play
class MyTestCase(unittest.TestCase):
    def test_connect_four(self):
        total_board = init(6, 7)

        fillBoard(total_board, 5, 2, player1)

        r, c = play(total_board, player2)
        d = {"row": c, "col": r}

        fillBoard(total_board, 5, 1, player1)

        r, c = play(total_board, player2)

if __name__ == '__main__':
    unittest.main()
