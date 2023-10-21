for _ in range(int(input())):
    n=int(input())
    a=list((input().split()))
    b=list((input().split()))
    aaa=[]
    bbb=[]
    aa=0
    bb=0
    for i in range(n):
        if a[i]!="0":
            aa+=1
        else:
            aaa.append(aa)
            aa=0
    aaa.append(aa)        
    for i in range(n):        
        if b[i]!="0":
            bb+=1
        else:
            bbb.append(bb)
            bb=0
    bbb.append(bb)        
    ma=max(aaa)
    mb=max(bbb)
    if ma>mb:
        print("Om")
    elif ma==mb:
        print("Draw")
    else:
        print("Addy")