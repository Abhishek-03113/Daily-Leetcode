n, k = map(int, input().split())
s = input()

target = k - 1

ans = []
swap = []

ones = 0
cnt = 0

ind = 0

for i in range(n):

    if s[i] == "1":
        ones += 1
    else:
        if ones > 0:
            cnt += 1
            ones = 0

    if cnt < target:
        ans.append(s[i])
    else:
        swap.append(s[i])


for i in range(len(swap)):

    if swap[i] == "1":
        swap[i] = -1
        ans.append("1")

    elif swap[i] == "0" and swap[i - 1] == -1:
        break

for i in range(len(swap)):

    if swap[i] != -1:
        ans.append(swap[i])

print(''.join(ans))
