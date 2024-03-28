from math import sqrt

memo = {}

def is_binary_decimal(n):
    n = str(n)
    for digit in n:
        if digit not in ['0', '1']:
            return False
    return True

def is_product_of_binary_decimals(n):
    if n in memo:
        return memo[n]

    if is_binary_decimal(n):
        memo[n] = True
        return True

    sqrt_n = int(sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            j = n // i
            if is_binary_decimal(i) and is_binary_decimal(j):
                memo[n] = True
                return True
            elif is_product_of_binary_decimals(j) and is_product_of_binary_decimals(i):
                memo[n] = True
                return True

    memo[n] = False
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    print("YES" if is_product_of_binary_decimals(n) else "NO")