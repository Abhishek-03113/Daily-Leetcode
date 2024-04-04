from collections import deque


def soln(n, a):

    ans = [0] * n
    c = 0
    for i in range(n):
        if a[i] > c:
            ans[c] += 1
            c += 1
        else:
            ans[a[i] - 1] += 1
            
    temp = n
    print(temp, end=" ")
    for i in range(n):
        temp -= ans[i]
        print(temp, end=" ")
        if temp == 0:
            break
    print()
    # print(0)

    # queue = deque(a)
    # b = []
    # time = 0
    # while queue:
    #     time += 1
    #     b.append(len(queue))
    #     queue.popleft()
    #     queue = deque(x - 1 for x in queue if x > 1)
    # b.append(0)
    # return b


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    soln(n, a)
    # print(*soln(n, a))
