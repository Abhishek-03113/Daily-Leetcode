# Function to calculate maximum total sales
def sol(N, sales):
    max_ = sales[0] * 2
    total_ = sales[0]

    for i in range(1, N):
        val = sales[i]
        mul = val * 2

       
        sum2 = total_ + mul
        total_ += val

        if sum2 > max_:
            max_ = sum2

    return max_

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        sales = list(map(int, input().split()))
        print(sol(n, sales))

if __name__ == "__main__":
    main()
