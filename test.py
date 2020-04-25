import unittest
from app import Game


class GameSpec(unittest.TestCase):

    def test_change_board(self):
        game = Game("hudson","tyler")
        game.change_turn()
        self.assertEqual(game.turn,"O")



    def test_won(self):
        WON_BOARD = [
        ["X","X","X"],
        ["*","*","*"],
        ["*","*","*"]
        ]

        WIN_BY_ROW = [
        ["X","X","X"],
        ["*","*","*"],
        ["*","*","*"]
        ]

        WIN_BY_COL = [
        ["X","O","*"],
        ["X","O","*"],
        ["*","O","X"]
        ]

        WIN_BY_DIV = [
        ["X","O","*"],
        ["O","X","*"],
        ["*","O","X"]
        ]

        NO_WIN = [
        ["X","O","X"],
        ["X","O","O"],
        ["O","X","X"]
        ]

        game = Game("hudson","tyler")
        self.assertEqual(game.win(),False)
        game.board.value = WON_BOARD
        self.assertEqual(game.win(),True)

if __name__ == '__main__':
    unittest.main()
