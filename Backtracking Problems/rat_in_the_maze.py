# Aluno: Angelo Garangau Menezes
# NUSP: 11413492

import ast

def check_available_move(x, y):
    if x >= 0 and x < length_maze and y >= 0 and y < length_maze and maze[x][y] == 1:
        return True
    return False

def search_maze(current_row, current_column, current_moves):
    
    if (current_row, current_column) == (length_maze-1,length_maze-1):
        solutions[str(current_moves)] = True
        return True
    
    if check_available_move(current_row, current_column):
        
        current_moves.append('D')
        search_maze(current_row+1, current_column, current_moves)
        current_moves.pop()
        
        current_moves.append('R')
        search_maze(current_row, current_column+1, current_moves)   
        current_moves.pop()

if __name__ == "__main__":
    
    n_test_cases = int(input())

    for _ in range(n_test_cases):

        length_maze = int(input())
        maze = input().split()
        maze = [int(i) for i in maze]
        maze = [maze[i:i+length_maze] for i in range(0, len(maze), length_maze)]
        solutions = {}

        search_maze(0,0,[])
        for key in solutions.keys():
            key = ast.literal_eval(key)
            print(''.join(key), end=' ')
        solutions = {}
        print('')
            