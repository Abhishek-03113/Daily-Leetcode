n = int(input())

nums = list(map(int, input().split()))


sums = (n * (n + 1)) // 2

s = sum(nums)

print(sums - s)
