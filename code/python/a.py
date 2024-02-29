def closest_power_of_2_less_than_n(n):
    if n <= 1:
        return 0 
    power = 1
    while power * 2 <= n:
        power *= 2
    return power
t = int(input()) 

for i in range(t):
    n = int(input()) 
    if n == 1:
        print(1)
    else:
        print(closest_power_of_2_less_than_n(n))
    