for _ in range(int(input())):

    n = int(input())

    if n % 2 == 1:
        print("NO")
        continue

    else:
        print("YES")
        for i in range(n // 2):
            print("AA", end="") if i % 2 == 0 else print("BB", end="")

        print()
