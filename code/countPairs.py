#User function Template for python3
def front(self,n,i,j):
    if j==n-1:
        i+=1
        j=0
    else:
        j+=1
    return i,j

def rear(self,n,i,j):
    if j==0:
        i-=1
        j=n-1
    else:
        j-=1
    return i,j


def is_valid(self,n,i,j,a,b):
    if i==n:
        return False
    if a==-1:
        return False
    return Trues