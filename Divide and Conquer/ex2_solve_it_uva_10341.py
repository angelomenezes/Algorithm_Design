import sys
from math import exp, sin, cos, tan

def equation(p, q, r, s, t, u, x):
    return p * exp(-x) + q * sin(x) + r * cos(x) + s * tan(x) + t * x ** 2 + u

def solve_it(sample_input):
    p, q, r, s, t, u = list(map(int, sample_input))
    EPS = 1E-6

    if equation(p, q, r, s, t, u, 1) > EPS:
        print('No solution')
        return 0

    low, high = 0.0, 1.0

    while abs(high - low) > EPS:
        mid = (high + low) / 2
        answer = equation(p, q, r, s, t, u, mid)
        if answer > 0:
            low = mid
        else:
            high = mid
    
    print('{:.4f}'.format(mid))

    return 0

if __name__ == "__main__":
    
    while True:
        try:
            sample_input = input().split() 
            solve_it(sample_input)

        except Exception:
            sys.exit(1)