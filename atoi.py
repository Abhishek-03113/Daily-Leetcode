 l=len(s)
        s1=""
        i=0
        sign=1
        if s[i]=='-':
            i+=1
            while i<l:
                s1+=s[i]
                i+=1
            sign=-1
            
        else:s1=s
            
        i=0
        l=len(s1)
        s=""
        if s1[i]=='0':
            while i<l:
                if s1[i]=='0':
                    i+=1
                else:break
            while i<l:
               s+=s1[i]
               i+=1
        else:s=s1
        i=0
        l=len(s)
        while i<l:
            if ord(s[i])>=48 and ord(s[i])<=57:
                i+=1
            else: return -1
        i=0
        ans=0
        while i<l:
            temp=ord(s[i])-48
            ans=ans*10+temp
            i+=1
        ans=ans*sign
        return ans
