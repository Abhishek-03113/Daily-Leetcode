
class Solution:
 
 
def sumBitDifferences(self,arr, n):
    # code here
        total_bits = 0
        
        # Iterate through each bit position
        for i in range(32):  # 32 bits for integers in Python
            set_bits_count = 0  # Count of set bits at this position
            
            # Count the number of set bits at this position
            for num in arr:
                if num & (1 << i):
                    set_bits_count += 1
            
            # Calculate bit differences at this position and add to total_bits
            unset_bits_count = n - set_bits_count
            total_bits += set_bits_count * unset_bits_count
        
        return total_bits * 2
