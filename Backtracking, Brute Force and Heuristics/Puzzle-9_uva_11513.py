import time
from queue import PriorityQueue
from itertools import chain

class Node:
    def __init__(self, data, level, cost_val, move=[]):
        self.data = data
        self.level = level
        self.cost_val = cost_val
        self.move = move
        self.size = 3
    
    def __lt__(self, visited_node): # For implementation of the priority queue
        return self.cost_val < visited_node.cost_val
    
    def shift(self, direction, index):
        node = [row[:] for row in self.data]
        if direction == 'H':
            node[index-1] = node[index-1][2:] + node[index-1][:2] 
        elif direction == 'V':
            node[0][index-1], node[1][index-1], node[2][index-1] = node[1][index-1], node[2][index-1], node[0][index-1]
        return node
    
    def generate_child(self):
        possible_directions = ['H', 'V']
        possible_positions = [1, 2, 3]
        children = []
        
        for direction in possible_directions:
            for position in possible_positions:
                child = self.shift(direction, position)
                move = [direction + str(position)]
                child_node = Node(child, self.level + 1, 0, self.move + move)
                children.append(child_node)
        return children

class Puzzle:
    def __init__(self):
        self.size = 3
        self.DEBUG = True
        self.open = []
        self.closed = []        

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
                if num != i*self.size + (j+1):
                    correct_row = (num - 1) // self.size
                    correct_col = (num - 1) % self.size
                    cost += abs(i - correct_row) + abs(j - correct_col)
        return cost
    
    def play(self):
        end_is_near = False

        while not end_is_near:
            puzzle = []
            for _ in range(self.size):
                sample_input = list(map(int, input().split()))
                if sample_input == [0]:
                    end_is_near = True
                    break
                puzzle.append(sample_input)

            if end_is_near:
                break

            start = Node(puzzle, 0, 0)
            start.cost_val = self.cost(start)
            
            open_queue = PriorityQueue()
            closed_nodes = set()

            open_queue.put(start)

            if not self.is_solvable(start.data):
                print('Not solvable')
                return 0

            while True:
                    
                current_node = open_queue.get()

                # In case the difference between the current node and the goal is zero
                # print the steps until the solution and break
                if self.is_solved(current_node):
                    print(''.join(current_node.move))
                    break
                
                for child in current_node.generate_child():
                    permutation_tuple = tuple(list(chain.from_iterable(child.data)))

                    if permutation_tuple not in closed_nodes:
                        child.cost_val = self.cost(child)
                        closed_nodes.add(permutation_tuple)
                        open_queue.put(child)

if __name__ == "__main__":
    
    puzzle = Puzzle()
    puzzle.play()
