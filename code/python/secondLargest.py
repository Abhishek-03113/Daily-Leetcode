def getSecondOrderElements(n: int, a: [int]) -> [int]:
    ans = [0, 0]
    max_ = float("-inf")
    max2 = float("-inf")
    min_ = float("inf")
    min2 = float("inf")

    for i in range(n):
        if a[i] > max_:
            max2 = max_
            max_ = a[i]
        elif a[i] > max2 and a[i] != max_:
            max2 = a[i]

        if a[i] < min_:
            min2 = min_
            min_ = a[i]

        elif a[i] < min2 and a[i] != min_:
            min2 = a[i]

    ans[0] = max2
    ans[1] = min2

    print(ans)
    return ans


n = int(input())

a = list(map(int, input().split()))

getSecondOrderElements(n, a)
# print(getSecondOrderElements(n,a))
# Output: [4, 2]
