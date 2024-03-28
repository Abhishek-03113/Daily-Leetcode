t = int(input())
for _ in range(t):
    n = int(input())
    side = 2*n
    board = [['#' if (i//2+j//2)%2==0 else '.' for j in range(side)] for i in range(side)]
    for row in board:
        print(''.join(row))