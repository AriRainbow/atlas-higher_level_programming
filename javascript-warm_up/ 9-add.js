#!/usr/bin/node

// Function to add two numbers
function add(a, b) {
  // Convert arguments to integers and return their sum
  return parseInt(a) + parseInt(b);
}

// Get the first and second arguments from the command line
const arg1 = process.argv[2]; // First argument
const arg2 = process.argv[3]; // Second argument

// Print the result of the addition using the add function
// If the argument cannot be converted to numbers, NaN will be printed
console.log(add(arg1, arg2));
