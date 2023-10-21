n = int(input())
a = [input() for _ in range(n)]
count = {}
for i in a:
    count[i] = count.get(i, 0) + 1
    print(count[i])
print(count)
print(len(count))
for i in count.values():
    print(i, end=" ")