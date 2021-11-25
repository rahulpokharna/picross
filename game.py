# The game of picross can be defined here

# Want numpy or Pandas most likely, probably pandas so I get used to it
import numpy as np

#? create game board
# class puzzle:
#     # Initialize it

#     # 

# Create from column and row lists 
#! This is the probability side of it, iterate and update the plot with the new probability/gradient color
def create_puzzle_list(columns, rows):
    puzzle = {
        'shape': (len(columns), len(rows))

    }

# def create_puzzle_board(board):

# Sample board that is 10x10
test_board = \
    [[1,1,1,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,0,1,0,0],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,1,0,0,1,1,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [1,1,1,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,1,1],
    [0,0,0,0,0,0,0,0,1,1]]
test_board = np.array(test_board)

# Determine colummns and rows that represent the data of the puzzle 
def eval_hints(board):
    print(board)
    # find columns and rows
    if len(board) == 0:
        return None

    # Rows, columns
    n, m = board.shape

    # View rows, get the number of 1s as a group linearly with gaps, 
    rows = []
    for row in board:
        rows.append(eval_list(row))

    cols = []
    for col in board.T:
        cols.append(eval_list(col))

    puzzle = {
        'shape': board.shape,
        'rows': rows,
        'cols': cols

    }
    return puzzle


    # View columns

def eval_list(lis):
    # Iterate along this list, get the number of 1s in a row
    out = []
    curr = 0

    # Iterate along list
    for x in lis:
        # If there is not a block (1)
        if x == 0:
            # see if a segment needs to be appended to the list
            if curr != 0:
                out.append(curr)
                curr = 0
        else:
            # If there is a 1 at this spot, append it to the current length of the segment
            curr += 1
    
    # If the last block is touching the wall, then make sure the final segment is appended
    if curr != 0 or len(out) == 0:
        out.append(curr)
        curr = 0

    # Ensure a [0]
    return out


print(eval_hints(test_board)) 

#* n by m board
#* per column per row array of inputs

#* processor to get the row array of inputs
#* or input of just drawing

# probability map of each square being a 1 or 0 (1 is filled, 0 is empty)

# Can do a visualization, at each step of probability check, change the color/plot of probabilities, goes from intermediate to solid

# Want to actually be able to play
# Find a way to make a solver as well? 



# Muolti Arm Bandit? Updatee posteriors