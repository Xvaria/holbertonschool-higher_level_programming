#!/usr/bin/node

// prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const myArgs = process.argv;
const newArgs = parseInt(myArgs[2]);
if (isNaN(newArgs)) {
  console.log('Not a number');
} else {
  console.log(newArgs);
}
