#!/usr/bin/node

const Rectangle = require('./4-rectangle'); // Import the Rectangle class

class Square extends Rectangle {
  // Constructor to initialize the square with size
  constructor (size) {
    super(size, size); // Call the constructor of Rectangle with size for both width and height
  }
}

module.exports = Square;
