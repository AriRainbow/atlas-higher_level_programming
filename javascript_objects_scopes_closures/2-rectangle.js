#!/usr/bin/node

class Rectangle {
  // Constructor to initialize the rectangle with width and height
  constructor (w, h) {
    // Check if w and h are positive integers greater than 0
    if (w > 0 && h > 0) {
      this.width = w; // Set width
      this.height = h; // Set height
    } else {
      // Create an empty object if conditions are not met
      return {};
    }
  }
}

module.exports = Rectangle;
