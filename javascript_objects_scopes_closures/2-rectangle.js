#!/usr/bin/node

class Rectangle {
  // Constructor to initialize the rectangle with width and height
  constructor (w, h) {
    // Check if w and h are positive integers greater than 0
    if (w > 0 && h > 0) {
      this.width = w; // Set width
      this.height = h; // Set height
    } else {
      // Set to an empty object when deminsions are invalid
      return {};
    }
  }

  // Mod to match the exact expected output
  toString () {
    if (this.width === undefined || this.height === undefined) {
      return 'Rectangle {}'; // Matches the exact output required
    }
    // Otherwise, return the string representation of the Rectangle object
    return `Rectangle { width: ${this.width}, height: ${this.height} }`;
  }
}

module.exports = Rectangle;
