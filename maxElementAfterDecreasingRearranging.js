/**
 * @param {number[]} arr
 * @return {number}
 */
var maximumElementAfterDecrementingAndRearranging = function(arr) {
    
    const n = arr.length; 
    arr.sort((a, b) => a - b);

    var ans = 1; 

    for (let i = 0; i<=n; i++)
    {

        if ( arr[i] >=  (ans + 1)){
            ans++ ; 
        }   
    }
    
    return ans
};
