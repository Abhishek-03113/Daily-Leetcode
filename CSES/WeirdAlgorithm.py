n = int(input())

ans = [n]

while n != 1:
    if n % 2 == 0:
        n = n / 2
        ans.append(int(n))
    else:
        n = n * 3 + 1
        ans.append(int(n))

for i in ans:
    print(i, end=" ")
