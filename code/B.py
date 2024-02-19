t = int(input()) 


for _ in range(t):
    n = int(input()) 
    arr =[]
    
    for i in range(n):
        s = input() 
        arr.append(s)
    
    # print(arr)
    prev = 0
    call = 0
    rows_cnt = []
    for i in range(n):
        if call > 2:
            break
        cnt = 0
        if '1' not in arr[i]:
            continue 
        else:
            for i in arr[i]:
                if i == '1':
                    cnt += 1
            rows_cnt.append(cnt)
            call += 1
    if rows_cnt[0] != rows_cnt[1]:
        print('TRIANGLE')
    else:
        print('SQUARE')