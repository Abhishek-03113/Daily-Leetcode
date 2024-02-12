class Solution:
    def sequence(self, n):
        # code here
        j=1
        s2=0
        for i in range(1,n+1):
            s=1
            k=i
            while k>0:
                s=(s*j)%((10**9)+7)
                k=k-1
                j=j+1
            s2=(s2+s)%((10**9)+7)
        return s2
