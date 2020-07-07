import unittest
from app import Game


class GameSpec(unittest.TestCase):

    def test_change_board(self):
        game = Game("hudson","tyler")
        game.change_turn()
        self.assertEqual(game.turn,"O")

    def test_find_corner(self):
        game = Game("hudson","tyler")
        board = [
        ["X","X","*"],
        ["*","*","*"],
        ["*","*","*"]
        ]
        game.board.value = board
        self.assertEqual(game.board.find_corner("X",Game.CORNERS),[0,0])


    def test_turn(self):
        game = Game("hudson","tyler")
        board = [
        ["X","X","X"],
        ["*","*","*"],
        ["*","*","*"]
        ]
        game.board.value = board
        self.assertEqual(game.board.turn(),4)

    def test_opposite_corner(self):
        game = Game("hudson","tyler")
        game.board.value = [
        ["X","X","X"],
        ["*","*","*"],
        ["*","*","*"]
        ]
        game.board.opposite_corner(0,0)
        self.assertEqual(game.board.opposite_corner(0,0),(2,2))

    def test_won(self):
        WIN_BY_FIRST_ROW = [
        ["X","X","X"],
        ["*","*","*"],
        ["*","*","*"]
        ]

        WIN_BY_SECOND_ROW = [
        ["*","*","*"],
        ["O","O","O"],
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
        game.turn = "X"
        self.assertEqual(game.game_won(),False)

        ## returns true if you have 3 "X" or "O" in a first row
        game.board.value = WIN_BY_FIRST_ROW
        game.turn = "X"
        self.assertEqual(game.game_won(),True)

        ## returns true if you have 3 "X" or "O" in a second row
        game.board.value = WIN_BY_SECOND_ROW
        game.turn = "O"
        self.assertEqual(game.game_won(),True)

        ## returns true if you have 3 "X" or "O" in a first column
        game.board.value = WIN_BY_FIRST_COL
        game.turn = "X"
        self.assertEqual(game.game_won(),True)

        ## returns true if you have 3 "X" or "O" in a first column
        game.board.value = WIN_BY_SECOND_COL
        game.turn = "O"
        self.assertEqual(game.game_won(),True)

        ## returns true if you have 3 "X" or "O" in a diagonal starting from the left
        game.board.value = WIN_BY_DIV_LEFT
        game.turn = "X"
        self.assertEqual(game.game_won(),True)

        ## returns true if you have 3 "X" or "O" in a diagonal starting from the right
        game.board.value = WIN_BY_DIV_RIGHT
        game.turn = "O"
        self.assertEqual(game.game_won(),True)

        ## returns false when there are no 3s in a row, col, or diagonal
        game.board.value = NO_WIN
        self.assertEqual(game.game_won(),False)

if __name__ == '__main__':
    unittest.main()
