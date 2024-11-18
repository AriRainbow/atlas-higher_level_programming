#!/usr/bin/node

class Rectangle {
  // Constructor to initialize the rectangle with width and height
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // If invalid dimensions, create an empty object
      return {};
    }
  }

  // Method to print the rectangle using 'X' characters
  print () {
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  // Method to rotate the rectangle (swap width and height)
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Method to double the size of the rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
