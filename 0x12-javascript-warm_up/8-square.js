#!/usr/bin/node

// prints a square

const myArgs = process.argv;
const newArgs = parseInt(myArgs[2]);
if (isNaN(newArgs)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < newArgs) {
    console.log('X'.repeat(newArgs));
    i++;
  }
}
