/*
@Abhishek 
Day 13 
Topic : Functional Programming js 

*/

/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    
	// return function(x) {

    //     for (i of functions.reverse())
    //     {
    //         x = i(x);
    //     }
        
    //     return x;

    // }

    const fn = (acc,f) => f(acc);

    return function(x)
    {
        return functions.reduceRight(fn,x)
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */ 


