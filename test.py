import unittest
from app import Game


class GameSpec(unittest.TestCase):

    def test_change_board(self):
        game = Game("hudson","tyler")
        game.change_turn()
        self.assertEqual(game.turn,"O")

if __name__ == '__main__':
    unittest.main()
