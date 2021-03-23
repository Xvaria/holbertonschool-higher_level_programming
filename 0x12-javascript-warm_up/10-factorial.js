#!/usr/bin/node

// computes and prints a factorial

function fact (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * fact(n - 1);
}
console.log(fact(parseInt(process.argv[2])));
