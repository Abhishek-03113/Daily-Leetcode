const obj = {
  a: 2,
  b: 3,
}

// destructure assignment
const { a, b } = obj;

console.log(a); // 2
console.log(b); // 3

const arr = ["Hello","World"];

const [c,d] = arr

console.log(c)
console.log(d)

// rest parameters 

function log(...args)
{
    console.log(args);
}

log(1,2,3,4,5,6,7,8,9,10);