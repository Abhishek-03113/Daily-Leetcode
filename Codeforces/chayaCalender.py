ans = []

t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    year = 0
    for y in a:
        year += 1
        if not year:
            year = y
            continue
        if y >= year:
            year = y
 
        elif y < year:
            
            year = (year-1)//y*y+y
 
    ans.append(year)
print(*ans,  sep="\n")