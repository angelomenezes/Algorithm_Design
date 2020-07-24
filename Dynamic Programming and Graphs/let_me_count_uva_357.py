def evaluate_change(money):
    coins = [1, 5, 10, 25, 50]
    array = [0] * 30001
    array[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], 30000):
            array[j] += array[j - coins[i]]
    return array

if __name__ == "__main__":
    
    while True:
        sample_input = int(input())

        ways = evaluate_change(sample_input)

        if ways[sample_input] == 1:
            print('There is only 1 way to produce {} cents change.'.format(sample_input))
        else:
            print('There are {} ways to produce {} cents change.'.format(ways[sample_input], sample_input))
    