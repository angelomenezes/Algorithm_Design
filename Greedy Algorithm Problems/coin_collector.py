def coin_selector(list_of_coins):
    
    coins = 2 # Minimum of possible coins
    last_sum = list_of_coins[0]

    for index in range(1, len(list_of_coins)-1):
        coin_sum = last_sum + list_of_coins[index] 
        if coin_sum < list_of_coins[index+1]:
            last_sum = coin_sum
            coins += 1 
    
    return coins 

if __name__ == "__main__":
    
    n_test_cases = int(input())

    for _ in range(n_test_cases):
    
        total_coins = int(input())

        list_of_coins = input().split()
        list_of_coins = [int(coins) for coins in list_of_coins]

        print(coin_selector(list_of_coins))

