cache={}
        def solve(row,col,k):
            if row>=n or col>=n or k<0:
                return 0
            if k==arr[row][col] and row==n-1 and col==n-1:
                return 1
            if ((row,col),k) in cache:
                return cache[((row,col),k)]
            else:
                cache[((row,col),k)]=solve(row+1,col,k-arr[row][col])+solve(row,col+1,k-arr[row][col])
            return cache[((row,col),k)]
        return solve(0,0,k)
