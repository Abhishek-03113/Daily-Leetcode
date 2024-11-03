def helper(ind, n, yn, memo):    
    if ind in memo:
        return memo[ind]
    if ind == n:
        return 0
    if yn[ind] < 0:
        memo[ind] = helper(ind + 1, n, yn, memo)
    else:
        memo[ind] = yn[ind]*yn[ind] + helper(ind + 1, n, yn, memo)
    return memo[ind]


def main(): 
    tests = int(input())
    for _ in range(tests):
        n = int(input())
        yn = list(map(int, input().split()))  
        memo = {}
        print(helper(0, n, yn, memo))

if __name__ == "__main__":
    main()
