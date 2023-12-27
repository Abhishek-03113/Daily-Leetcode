import os
from typing import *


def calibrationValues(line,answer):
    n = len(line)
    l,r = 0,0

    # line will be the string on the corresponding line in test case 
    for i in line:
        if i.isnumeric(): 
            l = i 
            break 
    
    for i in reversed(range(n)):

        if line[i].isnumeric():
            r = line[i]
            break 

    answer.append(int(str(l)+str(r)))

answer = []
tests = open("test.txt",'r')


while True: 
    test = tests.readline()
    calibrationValues(test,answer)
    
    if "" == test: 
        print("end of file")
        break

print(answer)
print(sum(answer))