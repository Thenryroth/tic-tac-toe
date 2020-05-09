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
    def game_won(self):
        print(self.board.value[0][0], self.board.value[0][1])
        	# first row
        if self.winning_board([[0,0],[0,1],[0,2]]):
            return True
        		# second row
        elif self.winning_board([[1,0],[1,1],[1,2]]):
            return True
        		# third row
        elif self.winning_board([[2,0],[2,1],[2,2]]):
            return True
        		# first column
        elif self.winning_board([[0,0],[1,0],[2,0]]):
            return True
        		# second column
        elif self.winning_board([[0,1],[1,1],[2,1]]):
            return True
        		# third column
        elif self.winning_board([[0,2],[1,2],[2,2]]):
            return True
        		# diagonal left to right
        elif self.winning_board([[0,0],[1,1],[2,2]]):
            return True
        # diagonal right to left
        elif self.winning_board([[0,2],[1,1],[2,0]]):
            return True
        return False

    def winning_board(self, board_positions):
        return self.board.value[board_positions[0][0]][board_positions[0][1]] == self.board.value[board_positions[1][0]][board_positions[1][1]] == self.board.value[board_positions[2][0]][board_positions[2][1]] == self.turn

      ### true or false


    def run_game(self):
        print("Hello! starting a new TicTacToe Game")
        self.board.show_board()
        first_move_row = int(input("Row "))
        first_move_col = int(input("Column "))
        first_move_value = input("Value ")

        self.board.mark_spot(first_move_row, first_move_col, first_move_value)
        self.board.show_board()
