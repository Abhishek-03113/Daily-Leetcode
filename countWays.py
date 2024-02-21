class Solution:

    def countWays(self, n, s):

        # code here

        dpTrue=[[0]*n for _ in range(n)]

        dpFalse=[[0]*n for _ in range(n)]

        

        mod=1003

        

        for i in range(0,n,2):

            if s[i]=="T":

                dpTrue[i][i]=1

                dpFalse[i][i]=0

            else:

                dpTrue[i][i]=0

                dpFalse[i][i]=1

        

        x=2

        while x<N:

            for i in range(0,n-x+1,2):

                for j in range(i+1,i+x,2):

                    if s[j]=="&":

                        dpTrue[i][i+x]+=dpTrue[i][j-1]*dpTrue[j+1][i+x]

                        dpFalse[i][i+x]+=dpFalse[i][j-1]*dpFalse[j+1][i+x]+dpFalse[i][j-1]*dpTrue[j+1][i+x]+dpTrue[i][j-1]*dpFalse[j+1][i+x]

                    elif s[j]=="|":

                        dpTrue[i][i+x]+=dpTrue[i][j-1]*dpTrue[j+1][i+x]+dpFalse[i][j-1]*dpTrue[j+1][i+x]+dpTrue[i][j-1]*dpFalse[j+1][i+x]

                        dpFalse[i][i+x]+=dpFalse[i][j-1]*dpFalse[j+1][i+x]

                    else:

                        dpTrue[i][i+x]+=dpTrue[i][j-1]*dpFalse[j+1][i+x]+dpFalse[i][j-1]*dpTrue[j+1][i+x]

                        dpFalse[i][i+x]+=dpTrue[i][j-1]*dpTrue[j+1][i+x]+dpFalse[i][j-1]*dpFalse[j+1][i+x]

                    dpTrue[i][i+x]=dpTrue[i][i+x]%mod

                    dpFalse[i][i+x]%=mod

            x+=2

        return dpTrue[0][n-1]%mod



