#!/usr/bin/node

// prints a message depending of the number of arguments passed

const myArgv = process.argv;
if (myArgv.length < 3) {
  console.log('No argument');
}
if (myArgv.length === 3) {
  console.log('Argument found');
}
if (myArgv.length > 3) {
  console.log('Arguments found');
}
