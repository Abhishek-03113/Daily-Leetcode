import math
import os
import random
import re
import sys
from collections import Counter

def migratoryBirds(arr):

    arr.sort()
    count = Counter(arr) 
    Most = max(count.values()) 
    
    for i in count: 
        
        if count[i] == Most:
            return i

