#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    hh,mm,ss = s.split(":")
    print(hh,mm,ss)
    meridian = ss[2:]

    mTime = ""
    mt = "00"
    
    if meridian == "PM":
        if hh == "12":
            mt = 12
        else:
            
            mt = int(hh)+12
    if meridian == "AM" and hh == "12":
        mt="00"
    elif meridian == "AM":
        mt = hh



    mTime = str(mt)+":"+mm+":"+ss[:2]

    print(mTime)
    
    
s = "12:00:00AM"
timeConversion(s)