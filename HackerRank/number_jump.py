# x1 = 
# v1 = 
# x2 = 
# v2 =  

x1,v1,x2,v2 = map(int,input().split())



def kangaroo(x1,v1,x2,v2):
    return("YES" if not v1==v2 and (x2-x1)%(v1-v2)==0 and (x2-x1)/(v1-v2)>0 else "NO")

    pass