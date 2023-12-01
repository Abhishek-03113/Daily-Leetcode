/**
 * @param {number[]} arr
 * @return {number}
 */
var maximumElementAfterDecrementingAndRearranging = function(arr) {
    arr.sort((a, b) => a - b);
    var ans = 1; 
    for (let i = 1; i<arr.length; i++)
    {
        if ( arr[i] >=  (ans + 1)){
            ans++ ; 
        }   
    }
    
    return ans
};
