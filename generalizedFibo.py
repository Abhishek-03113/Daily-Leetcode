#User function Template for python3



class Solution:

    def mul(self, res, mat,m):

        temp_res=[[0]*3 for _ in range(3)]

        for i in range(3):

            for j in range(3):

                for k in range(3):

                    temp_res[i][j]+=res[i][k]*mat[k][j]

                    temp_res[i][j]%=m

        for i in range(3):

            for j in range(3):

                res[i][j]=temp_res[i][j]

    def exp(self, n, m):

        while n>0:

            if n & 1:

                self.mul(self.res,self.mat,m)

            self.mul(self.mat,self.mat,m)

            n//=2

    def genFibNum(self, a, b, c, n, m):

        # code here 

        if n<=2:

            return 1%m

        self.mat=[[0]*3 for _ in range(3)]

        self.mat[0][0]=a

        self.mat[0][1]=b

        self.mat[0][2]=self.mat[1][0]=self.mat[2][2]=1

        self.res=[[0]*3 for _ in range(3)]

        self.res[0][0]=self.res[1][1]=self.res[2][2]=1

        

        self.exp(n-2,m)

        

        return (self.res[0][0]+self.res[0][1]+c*self.res[0][2])%m



#{ 

 # Driver Code Starts

#Initial Template for Python 3



if __name__ == '__main__': 

    t = int (input ())

    for _ in range (t):

        a,b,c,n,m=map(int,input().split())

        

        ob = Solution()

        print(ob.genFibNum(a,b,c,n,m))

# } Driver Code Ends
