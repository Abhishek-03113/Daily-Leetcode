def Chocholate(n,k):
    
    a = list(map(int,input().split()))
    

    chocolates = sum(a)

    if k == 0: print('Yes' if chocolates%n == 0 and chocolates > 0 else 'No')
    else: print('Yes' if chocolates >= n else 'No')

