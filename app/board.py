NUMBER_OF_ROWS = 3
NUMBER_OF_COLUMNS = 3
EMPTY_ROW = "*"
ROW_SEPARATOR = " | "
STARTING_BOARD = [
    ["*","*","*"],
    ["*","*","*"],
    ["*","*","*"]
]
# board
# functions
# win, tie, mark_sport, show, clear
class Board:
    def __init__(self):
        self.value = STARTING_BOARD

    def show_board(self):
        for row in self.value:
            row_display = ROW_SEPARATOR.join([cell for cell in row])
            print(row_display)

    def mark_spot(self,row,col,value):
        self.value[row][col]= value
        return self.value

    def turn(self):
        turn_number = 10
        for row in self.value:
            for cell in row:
                if cell == "*":
                    turn_number -= 1
        return turn_number
    def opposite_corner(self,row,col):
        if row == 0 and col == 0:
            OPPOSITE_CORNER= (2,2)
        elif row == 2 and col == 2:
            OPPOSITE_CORNER= (0,0)
        elif row == 0 and col == 2 or row == 2 and col == 0::
            OPPOSITE_CORNER= (col,row)
        return OPPOSITE_CORNER

# Given a Board, a position, and a value(x, or O) puts the
#value at that position on the board
# Mark position 0,0 with an X
# Returns
#  X | * | *
#  * | * | *
#  * | * | *
