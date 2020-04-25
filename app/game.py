 # Turn
 # Player1 Player2
 # Board
from .board import Board

class Game:

    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = "X"
        self.board = Board()

    def change_turn(self):
        if  self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    ## Ways to Win - Given a board return True if game won otherwise False
# If all values in the row are the same
# If all values in a column are the same
    def win(self):
        print(self.board.value[0][0], self.board.value[0][1])
        if self.board.value[0][0] == self.board.value[0][1] == self.board.value[0][2] == "X" or self.board.value[0][0] == self.board.value[0][1] == self.board.value[0][2] == "O":
            return True
        return False
    def run_game(self):
        print("Hello! starting a new TicTacToe Game")
        self.board.show_board()
        first_move_row = int(input("Row "))
        first_move_col = int(input("Column "))
        first_move_value = input("Value ")

        self.board.mark_spot(first_move_row, first_move_col, first_move_value)
        self.board.show_board()
