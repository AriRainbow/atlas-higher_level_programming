#!/usr/bin/node

class Rectangle {
  // Constructor to initialize the rectangle with width and height
  constructor (w, h) {
    // Check if w and h are positive integers greater than 0
    if (w > 0 && h > 0) {
      this.width = w; // Set width
      this.height = h; // Set height
    } else {
      // If conditions are not met, create a 'broken' Rectangle instance
      this.width = undefined;
      this.height = undefined;
    }
  }

  // Define a method to return a string representation of the Rectangle
  toString () {
    if (this.width && this.height) {
      return `Rectangle { width: ${this.width}, height: ${this.height} }`;
    }
    return 'Rectangle { invalid dimentions }';
  }
}

module.exports = Rectangle;
