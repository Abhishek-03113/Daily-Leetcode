for _ in range(int(input())):

    n = int(input())
    s = input()

    n = len(s)

    flg = 0

    for i in range(0, n // 2):

        if ord(s[i]) == ord(s[n - i - 1]):
            continue
        if ord(s[i]) > ord(s[n - i - 1]):
            flg = 1
        else:
            break

    rev = s[::-1]

    if flg:
        print(rev + s)
    else:
        print(s)
