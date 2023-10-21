"""Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable."""

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

    

def plusMinus(arr):
    p,n,z = 0
    k = len(arr)
    for i in range(k):
        if i<0:
            n+=1
        elif i>0:
            p+=1
        elif i == 0:
            z+=1
    pr = p/k
    nr = n/k 
    zr = z/k
    
    print("{0:.6f}".format(pr))
    print("{0:.6f}".format(nr))
    print("{0:.6f}".format(zr))
    
    pass



plusMinus(arr)