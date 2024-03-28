t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    count_a = [0]*3
    count_b = [0]*3
    for i in range(n):
        count_a[ord(a[i])-ord('a')] += 1
        count_b[ord(b[i])-ord('a')] += 1
    for i in range(3):
        if count_a[i] < count_b[i]:
            print("No")
            break
    else:
        print("Yes")