#!/usr/bin/node

// prints the addition of 2 integers

function add(a, b) {
  console.log(a + b);
}

const myArgs = process.argv;
const a = parseInt(myArgs[2]);
const b = parseInt(myArgs[3]);
if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  add(a, b);
}
