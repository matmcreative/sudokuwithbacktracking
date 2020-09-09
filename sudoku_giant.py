board = [
    [12,10,0,6,0,0,20,0,4,0,0,0,0,21,1,0,0,2,0,11,0,8,0,9,24],
    [18,7,9,0,1,22,25,0,0,0,0,23,24,4,0,0,8,19,0,6,0,0,12,0,10],
    [0,0,24,0,0,17,10,15,0,6,0,0,8,0,2,0,1,0,25,7,14,0,0,18,0],
    [4,2,0,3,0,0,0,0,0,7,0,0,12,0,15,0,0,5,0,0,0,0,0,0,0],
    [0,0,0,0,17,8,0,5,0,1,14,6,0,19,0,22,0,4,13,0,0,15,11,0,0],
    [0,15,2,5,0,18,0,0,14,0,0,21,20,1,3,0,0,0,22,0,0,0,0,0,9],
    [0,0,0,0,0,21,0,8,12,0,9,0,23,0,10,0,0,0,0,25,0,18,2,17,0],
    [0,0,0,0,0,0,19,16,11,0,0,22,0,0,0,0,0,0,15,0,0,13,14,0,0],
    [6,21,7,0,0,0,23,0,0,10,0,0,16,0,12,0,0,0,3,0,0,0,0,0,0],
    [0,0,0,20,0,1,0,0,13,0,25,0,0,7,14,0,11,0,4,0,21,0,0,5,12],
    [10,22,0,0,7,0,1,0,0,0,0,11,5,0,16,21,4,13,19,0,0,0,0,23,14],
    [0,0,0,21,0,4,0,0,0,24,0,18,0,0,25,12,0,142,0,3,0,8,16,0],
    [0,0,4,0,0,0,0,0,5,0,0,8,3,0,0,20,0,6,23,8,18,0,0,7,0],
    [0,0,0,16,0,0,0,10,0,0,0,0,15,0,8,0,0,0,7,0,13,0,25,20,5],
    [3,0,23,0,14,2,9,0,7,0,0,0,0,0,17,0,16,0,0,0,1,10,0,6,0],
    [0,0,0,0,21,0,0,2,0,0,0,0,0,10,5,0,15,0,0,1,0,17,0,0,0],
    [0,8,0,0,0,10,0,9,20,0,6,0,0,25,0,0,12,24,0,0,0,0,0,0,15],
    [0,0,0,0,0,13,0,0,0,0,17,3,21,0,4,18,0,0,0,5,0,19,7,11,23],
    [0,16,0,2,0,14,0,23,0,0,24,19,0,0,7,4,21,22,0,13,0,0,0,0,0],
    [11,4,0,17,0,0,0,0,6,18,0,12,0,0,0,0,23,25,0,19,0,0,0,2,13],
    [0,0,21,23,8,0,5,0,0,9,0,0,1,3,11,0,25,0,0,18,17,16,20,13,0],
    [0,5,0,0,0,0,0,19,24,0,7,0,0,0,21,0,0,0,0,20,0,6,3,10,0],
    [0,0,0,0,3,12,0,1,0,0,8,14,18,20,0,16,0,0,0,0,0,11,0,0,0]
]

def solve(brd):
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,26):
        if valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0

    return False


def valid(brd, num, pos):
    # Check row
    for i in range(len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 5
    box_y = pos[0] // 5

    for i in range(box_y*5, box_y*5 + 5):
        for j in range(box_x*5, box_x*5 + 5):
            if brd[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(brd):
    for i in range(len(brd)):
        if i % 5 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

        for j in range(len(brd[0])):
            if j % 5 == 0 and j != 0:
                print(" | ", end="")

            if j == 24:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")


def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board,'02')
solve(board)
print("___________________")
print_board(board)