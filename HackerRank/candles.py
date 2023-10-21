from collections import Counter

def birthdayCakeCandles(candles):
    m = max(candles)
    
    count = Counter(candles)
    print(count)
    return count[m]
    # Write your code 


candles = [3,2,1,3]

print(birthdayCakeCandles(candles))