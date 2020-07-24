from math import factorial
from itertools import groupby

def get_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i == 1:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    try:
        while True:
            sample_input = int(input())

            if sample_input == 0:
                break

            n_factorial = factorial(sample_input)

            n_factors = get_factors(n_factorial)

            prime_factor_list = [len(list(group)) for key, group in groupby(n_factors)]
            
            print(sample_input, end='')
            print('! = ', end='')
            print(*prime_factor_list)
    except:
        pass
