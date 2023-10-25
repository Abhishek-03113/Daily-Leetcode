/*
@Abhishek 
Day 15 
Topic : Javascript args ..
*/


/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
	var count =0 ; 

    return args.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */
