import unittest
from app import Game


class GameSpec(unittest.TestCase):

    def test_change_board(self):
        game = Game("hudson","tyler")
        game.change_turn()
        self.assertEqual(game.turn,"O")



    def test_won(self):
        WIN_BY_FIRST_ROW = [
        ["X","X","X"],
        ["*","*","*"],
        ["*","*","*"]
        ]

        WIN_BY_SECOND_ROW = [
        ["*","*","*"],
        ["X","X","X"],
        ["*","*","*"]
        ]

        WIN_BY_FIRST_COL = [
        ["X","O","*"],
        ["X","O","*"],
        ["X","*","X"]
        ]

        WIN_BY_SECOND_COL = [
        ["X","O","*"],
        ["X","O","*"],
        ["*","O","X"]
        ]

        WIN_BY_DIV_LEFT = [
        ["X","O","*"],
        ["O","X","*"],
        ["*","O","X"]
        ]
        WIN_BY_DIV_RIGHT = [
        ["X","*","O"],
        ["X","O","*"],
        ["O","*","X"]
        ]

        NO_WIN = [
        ["X","O","X"],
        ["X","O","O"],
        ["O","X","X"]
        ]

        ## should return false for a blank Board
        game = Game("hudson","tyler")
        self.assertEqual(game.win(),False)

        ## returns true if you have 3 "X" or "O" in a first row
        game.board.value = WIN_BY_FIRST_ROW
        self.assertEqual(game.win(),True)

        ## returns true if you have 3 "X" or "O" in a second row
        game.board.value = WIN_BY_SECOND_ROW
        self.assertEqual(game.win(),True)

        ## returns true if you have 3 "X" or "O" in a first column
        game.board.value = WIN_BY_FIRST_COL
        self.assertEqual(game.win(),True)

        ## returns true if you have 3 "X" or "O" in a first column
        game.board.value = WIN_BY_SECOND_COL
        self.assertEqual(game.win(),True)

        ## returns true if you have 3 "X" or "O" in a diagonal starting from the left
        game.board.value = WIN_BY_DIV_LEFT
        self.assertEqual(game.win(),True)

        ## returns true if you have 3 "X" or "O" in a diagonal starting from the right
        game.board.value = WIN_BY_DIV_RIGHT
        self.assertEqual(game.win(),True)

        ## returns false when there are no 3s in a row, col, or diagonal
        game.board.value = NO_WIN
        self.assertEqual(game.win(),False)

if __name__ == '__main__':
    unittest.main()
