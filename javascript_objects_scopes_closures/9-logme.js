#!/usr/bin/node

// Initialize a counter to keep track of the number of arguments printed
let counter = 0;

// Function to log the argument with the counter
exports.logMe = function (item) {
  console.log(`${counter}: ${item}`);
  counter++; // Increment the counter after printing the argument
};
