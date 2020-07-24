mem = [[-1 for _ in range(100)] for _ in range(100)]

def luggage_splitter(weights, weight_goal, current_item):
    global mem
    mx = 0
    if mem[weight_goal][current_item] != -1:
        return mem[weight_goal][current_item]
    
    for index in range(current_item, len(weights)):
        if weights[index] <= weight_goal:
            current_weight = weights[index] + luggage_splitter(weights, weight_goal-weights[index], index+1) 
            if mx < current_weight:
                mx = current_weight
    mem[weight_goal][current_item] = mx
    return mx

if __name__ == "__main__":
    n_of_cases = int(input())

    for _ in range(n_of_cases):
        weights = list(map(int, input().split()))
    
        if sum(weights) % 2 != 0:
            print('NO')
            continue
        
        total_itens = len(weights)
        max_weight = sum(weights) // 2
        
        if luggage_splitter(weights, max_weight, 0) == max_weight:
            print('YES')
        else:
            print('NO')


          