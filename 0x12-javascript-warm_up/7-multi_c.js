#!/usr/bin/node

// prints x times C is fun

const myArgs = process.argv;
const newArgs = parseInt(myArgs[2]);
if (isNaN(newArgs)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < newArgs) {
    console.log('C is fun');
    i++;
  }
}
