#!/usr/bin/node

const Square = require('./5-square'); // Import the Square class from 5-square.js

class SquareExt extends Square {
  // Constructor to initialize the square with size
  constructor (size) {
    super(size); // Call the constructor of Square (which calls Rectangle's constructor)
  }

  // Method to print the square using the specified character (default is 'X')
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = SquareExt;
