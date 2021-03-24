#!/usr/bin/node

// returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let noo = 0;
  list.forEach(item => {
    if (item === searchElement) {
      noo++;
    }
  });
  return (noo);
};
