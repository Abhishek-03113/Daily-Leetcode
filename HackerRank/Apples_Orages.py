# s-t == house area 
# point a == apple tree b == orange tree 
# fruit lands d units form tree 
#  for orange tree d = -ve 
# for apple tree d = +ve
# given values of d for m apples and n oranges 
# function returns how many apples and oranges land on sam's house i.e. in [s,t]
# The Whole parameter is a x-axis 
# s,t = map(int,input().split())
# a,b, = map(int,input().split())
# m,n = map(int,input().split())

# apples = list(map(int,input().split()))
# oranges = list(map(int,input().split()))


def countApplesandOrange(s,t,a,b,apples,oranges):
    x,y = len(apples),len(oranges)

    minDA= abs(s-a)
    minDO= abs(b-t)
    ca =0
    co = 0 

    for i in range(x):
        if apples[i]>0 and apples[i]>=minDA:
            ca += 1
    for i in range(y):
        if oranges[i]<0 and abs(oranges[i])>=minDO:
            co+=1

    print(ca,"\n",co)


first_multiple_input = input().rstrip().split()

s = int(first_multiple_input[0])

t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()

a = int(second_multiple_input[0])

b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()

m = int(third_multiple_input[0])

n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesandOrange(s, t, a, b, apples, oranges)


    