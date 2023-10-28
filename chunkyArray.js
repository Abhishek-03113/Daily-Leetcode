/*
@Abhishek 
day 18 
topic : JavaScript Array sliciing 
*/
/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */

var chunk = function(arr, size) {

    let chunkArray = [];

    let index = 0 

    while (index < arr.length)
    {
        chunkArray.push(arr.slice(index,index+size));
        index += size;

    }

    return chunkArray;


    
};

