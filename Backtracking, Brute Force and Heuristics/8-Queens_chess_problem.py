# Aluno: Angelo Garangau Menezes
# NUSP: 11413492

import ast

def check_place(positions, rows, column):
    for i in range(rows):
        if positions[i] == column:
            return False
        if positions[i] - i == column - rows:
            return False
        if positions[i] + i == column + rows:
            return False
    return True
    
def create_chessboard(positions):
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    
    for column, index in enumerate(positions):
        board[index-1][column] = 1
    return board

def get_all_queen_solutions(positions, current_row):
    if current_row == board_shape:
        positions = [i+1 for i in positions]
        possible_solutions[str(positions)] = True
    else:
        for column in range(board_shape):
            if check_place(positions, current_row, column):
                positions[current_row] = column
                get_all_queen_solutions(positions, current_row + 1)

if __name__ == "__main__":
    
    n_test_cases = int(input())

    board_shape = 8
    possible_solutions = {}
    list_solutions = []
    positions = [0]*board_shape
    get_all_queen_solutions(positions, 0)

    for _ in range(n_test_cases):
        
        input_set = input().split()
        
        print('SOLN       COLUMN')
        print(' #      1 2 3 4 5 6 7 8')
        print(' ')

        case = 0
        for key in possible_solutions.keys():
            if ast.literal_eval(key)[int(input_set[1]) - 1] == int(input_set[0]):
                case += 1
                print(' ', end='')
                print(case, end = '      ')
                print(*list(ast.literal_eval(key)), sep = ' ')