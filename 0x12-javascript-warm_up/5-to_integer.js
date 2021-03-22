#!/usr/bin/node

// prints My number: <first argument converted in integer> if the first argument can be converted to an integer

const myArgs = process.argv;
if (myArgs.length !== 3) {
  console.log('Not a number');
} else {
  const newArgs = parseInt(myArgs[2]);
    if (isNaN(newArgs)) {
      console.log('Not a number');
    } else {
      console.log(newArgs);
    }
}
