for _ in range(int(input())):


    n = int(input())
    s = list(input())

    open = 0

    for i in range(n):

        if s[i] == '(':
            open += 1

        if s[i] == '_' and open > 0:
            s[i] = ')'
            open -= 1
        elif s[i] == '_' and open == 0:
            s[i] = '('
            open += 1
        elif s[i] == ")":
            open-=1

    stack = []

    ans = 0

    for i in range(n):
        if s[i] == '(':
            stack.append(i)
        else:
            ans += (i-stack.pop())
    print(ans)
