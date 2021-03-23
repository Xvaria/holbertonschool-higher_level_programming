#!/usr/bin/node

// class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const Squarec = require('./5-square');
class Square extends Squarec {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    let i = 0;
    while (i < this.height) {
      console.log(c.repeat(this.width));
      i++;
    }
  }
}

module.exports = Square;
