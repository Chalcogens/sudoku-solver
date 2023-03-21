def find_next_empty(puzzle):
    # finds next row, col that's unfilled == -1
    # return row, col tuple, or None if puzzle is complete
    for r in range(9):
        for c in range(8):
            if puzzle[r][c] == -1:
                return(r,c)
    return None, None #if puzzle is complete

def is_valid(puzzle, guess, row, col):
    #returns True if guess is valid, else False

    #check rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #check columns
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False

    #check boxes
    row_start = row//3 * 3
    col_start = col//3 * 3
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if puzzle[i][j] == guess:
                return False

    return True





def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # puzzle is represented by 9 lists containing 9 elements each. Empty squares == -1
    # returns whether a solution exists
    # if solution exists, updates (mutates) list with solution

    #step 1: choose somewhere on the puzzle to make a guess
    row,col = find_next_empty(puzzle)
    #step 1.1: check if puzzle is complete
    if row is None:
        return True
    #step 2: make a guess for the empty square
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True

    #step 3: backtrack and try a new number if an error occurs again
        puzzle[row][col] = -1

    #step 4: if all numbers are invalid, then puzzle is insolvable
    return False

if __name__ == "__main__":
    example_board = [
        [3, 9, -1, -1, 5, -1, -1, -1, -1],
        [-1, -1, -1, 2, -1, -1, -1, -1, 5],
        [-1, -1, -1, 7, 1, 9, -1, 8, -1],

        [-1, 5, -1, -1, 6, 8, -1, -1, -1],
        [2, -1, 6, -1, -1, 3, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 4],

        [5, -1, -1, -1, -1, -1, -1, -1, -1],
        [6, 7, -1, 1, -1, 5, -1, 4, -1],
        [1, -1, 9, -1, -1, -1, 2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)

