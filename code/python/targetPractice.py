"""Hard Coded Approach"""

target = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 4, 4, 4, 3, 2, 1],
    [1, 2, 3, 3, 3, 3, 3, 3, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


for _ in range(int(input())):
    n = 10
    s = []
    score = 0

    for i in range(10):
        s.append(input())

    for i in range(10):
        for j in range(10):
            if s[i][j] == "X":
                score += target[i][j]
    print(score)