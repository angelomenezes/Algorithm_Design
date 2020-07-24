def knapshack(i, current_weight, capacity):
    global mem

    if i == n_of_objects:
        return 0

    if mem[i][current_weight] != -1:
        return mem[i][current_weight]

    if current_weight + obj_weight[i] <= capacity:
        current_price = obj_price[i] + knapshack(i+1, current_weight + obj_weight[i], capacity)
    else:
        current_price = 0

    mem[i][current_weight] = max(current_price, knapshack(i+1, current_weight, capacity))

    return mem[i][current_weight]

if __name__ == "__main__":

    n_of_cases = int(input())

    for _ in range(n_of_cases):
        max_value_of_goods = 0

        n_of_objects = int(input())
        obj_weight = [0] * n_of_objects
        obj_price = [0] * n_of_objects

        for i in range(n_of_objects):
            obj_price[i], obj_weight[i] = list(map(int, input().split()))
        
        n_of_people = int(input())
        person_weight = [0] * n_of_people

        for i in range(n_of_people):
            mem = [[-1 for _ in range(1001)] for _ in range(1001)]
            person_weight = int(input())
            max_value_of_goods += knapshack(0, 0, person_weight)
        
        print(max_value_of_goods)

