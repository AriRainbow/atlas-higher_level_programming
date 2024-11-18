#!/usr/bin/node

const Square = require('./5-square'); // Import the Square class from 5-square.js

class SquareExt extends Square {
  // Method to print the square using the specified character (default is 'X')
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = SquareExt;
