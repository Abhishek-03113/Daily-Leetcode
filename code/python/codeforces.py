def solve():

    n,k = map(int, input().split()) 
    a = list(map(int,input().split())) 
    
    # a, b = map(int, input().split())
    # c, d = map(int, input().split())

    # ans = 0

    # # print(f"Alice {a, b}  bob {c , d}")
    # if a == c:

    #     if b == d:
    #         print(b - a)
    #         return

    #     print(min(b, d) - a + 1)

    # elif a < c:

    #     if b < c:
    #         print(c - b)
    #         return
    #     elif b == c:
    #         print(1)
    #     elif b > c:
    #         if b == d:
    #             print(b - c + 1)

    #         elif b > d:
    #             print(b - c)

    # elif a > c:

    #     if d > b:
    #         print(3)
    #         return
    #     elif d == b:
    #         print(d - c + 1)
    #         return
    #     else:
    #         print(d - c + 1)
    #         return


for _ in range(int(input())):
    solve()
