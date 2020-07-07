 # Turn
 # Player1 Player2
 # Board
from .board import Board

class Game:
    CORNERS = [[0,0],[2,0],[2,2],[0,2]]
    EDGES = [[0,1],[2,1],[1,0],[1,2]]

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

    def execute_turn(self, row = None, col = None):
        print(self.turn + "turn")
        if row == None:
            row = int(input("Row"))
        if col == None:
            col = int(input("Column "))
        self.board.mark_spot(row, col, self.turn)


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
    def game_over(self):
        star_counter  = 0
        for row in self.board.value:
            if "*" in row:
                star_counter += 1
        return (self.game_won()) or (star_counter == 0)

    def computer_move(self):
        if turn == 3:
            if player2 in EDGES:
                self.execute_turn(CORNERS[0][0],CORNERS[0][1])
            else:
                
                self.execute_turn(OPPOSITE_CORNER)


    ## functions we need
    ## GET NUMBER TURN FUNCTION
    ## GET OPPOSITE CORNER FUNCTION
    ## Player class - to determine if player is human or computer```

    def run_game(self):
        print("Hello! starting a new TicTacToe Game")
        self.board.show_board()
        self.execute_turn()
        print(self.board.show_board())
        while self.game_over() == False:
            self.change_turn()
            self.execute_turn()
            print(self.board.show_board())
        if self.game_won():
            print(f"Player {self.turn}, YOU WON THE GAME")
