import time
from queue import PriorityQueue
from itertools import chain

class Node:
    def __init__(self, data, level, cost_val, move=""):
        self.data = data
        self.level = level
        self.cost_val = cost_val
        self.move = move
        self.size = 4
    
    def __lt__(self, visited_node): # For implementation of the priority queue
        return self.cost_val < visited_node.cost_val

    def generate_child(self):
        x,y = self.find_zero(self.data, 0)
        possible_moves = [[x, y - 1],[x, y + 1],[x - 1, y],[x + 1, y]]
        children = []
        last_move = ''
        
        for move, position in enumerate(possible_moves):
            child = self.make_move(self.data, x, y, position[0], position[1])
            if child is not None:
                if move == 0:
                    last_move = 'L'
                elif move == 1:
                    last_move = 'R'
                elif move == 2:
                    last_move = 'U'
                elif move == 3:
                    last_move = 'D'
                child_node = Node(child, self.level + 1, 0, self.move + last_move)
                children.append(child_node)
        return children
        
    def make_move(self, puzzle, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            moved_puzzle = []
            moved_puzzle = self.copy(puzzle)
            moved_puzzle[x2][y2], moved_puzzle[x1][y1] = moved_puzzle[x1][y1], moved_puzzle[x2][y2]
            return moved_puzzle
        else:
            return None
        
    def copy(self, node): # For getting copy of node
        return [row[:] for row in node]
            
    def find_zero(self, puzzle, x):
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puzzle[i][j] == x:
                    return i, j

class Puzzle:
    def __init__(self):
        self.size = 4
        self.DEBUG = False
        self.open = []
        self.closed = []
        
    def get_input(self):
        puzzle = []
        for _ in range(0, self.size):
            sample_input = list(map(int, input().split()))
            puzzle.append(sample_input)
        return puzzle

    def count_inversions(self, array):
        count = 0
        size = self.size * self.size
        for i in range(size-1):
            for j in range(i+1, size):
                if array[i] != 0 and array[j] != 0 and array[i] > array[j]:
                    count += 1
        return count

    def is_solved(self, puzzle):
        if self.h(puzzle.data) == 0:
            return True
        return False
        
    def is_solvable(self, puzzle):
        zero_pos = -1
        for i in range(self.size):
            for j in range(self.size):
                if puzzle[i][j] == 0:
                    zero_pos = i

        inversions = self.count_inversions([num for row in puzzle for num in row])

        return (zero_pos % 2 == 0 and inversions % 2 == 1) or (zero_pos % 2 == 1 and inversions % 2 == 0)

    def print_node(self, node):
        for i in node.data:
            for j in i:
                print(j, end=' ')
            print('')
        print('')
        
    def cost(self, node): # Cost(x) = h(x) + g(x)
        return self.h(node.data) + node.level
    
    def h(self, start): # Calculate the distance to the goal using Manhatan distance
        cost = 0
        for i in range(self.size):
            for j in range(self.size):
                num = start[i][j]
                if num != i*self.size + (j+1) and num != 0:
                    correct_row = (num - 1) // self.size
                    correct_col = (num - 1) % self.size
                    cost += abs(i - correct_row) + abs(j - correct_col)
        return cost
    
    def play(self):
        start = self.get_input()

        start = Node(start, 0, 0)
        start.cost_val = self.cost(start)
        
        open_queue = PriorityQueue()
        closed_nodes = set()

        open_queue.put(start)

        if not self.is_solvable(start.data):
            print('This puzzle is not solvable.')
            return 0

        while True:
                
            current_node = open_queue.get()

            # In case the difference between the current node and the goal is zero
            # print the steps until the solution and break
            if self.is_solved(current_node):
                print(current_node.move)
                break
            
            for child in current_node.generate_child():
                permutation_tuple = tuple(list(chain.from_iterable(child.data)))
                
                if permutation_tuple not in closed_nodes:
                    child.cost_val = self.cost(child)
                    closed_nodes.add(permutation_tuple)
                    open_queue.put(child)

            if len(current_node.move) > 50:
                print('This puzzle is not solvable.')
                break

            if self.DEBUG:
                self.print_node(current_node)
                print('')

if __name__ == "__main__":
    
    n_of_cases = int(input())
    #start = time.time()
    for _ in range(n_of_cases):
        puzzle = Puzzle()
        puzzle.play()
    #stop = time.time()
    #print('Time spent: {:.4f}s'.format(stop - start))