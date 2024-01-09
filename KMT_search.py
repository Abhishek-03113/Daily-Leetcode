lass Solution:
    def search(self, pat, txt):
        # code here
        l = 0
        indexs = []

        while l < len(txt):
            if txt[l] == pat[0] and txt[l:l+len(pat)] == pat:
                    indexs.append(l + 1)
            l += 1

        if indexs:
            return indexs
        else:
            return [-1]
        
