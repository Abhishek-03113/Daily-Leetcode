  li = [None] * (len(s)+1)
        li2 = [None]*(len(s)+1)
        
        if len(s)%2 != 0:
            halflen = len(s)//2+1
        else:
            halflen = len(s)//2

        for i in range(len(s)):
            li[i] = s[i]
        
        for i in range(r):
            for j in range(halflen):
                if li[j]=='1':
                    li2[j*2] = '1'
                    li2[j*2+1] = '0'
                else:
                    li2[j*2] = '0'
                    li2[j*2+1] = '1'
            li,li2 = li2,li

        return li[n]

