#!/usr/bin/node

// class Square that defines a square and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
