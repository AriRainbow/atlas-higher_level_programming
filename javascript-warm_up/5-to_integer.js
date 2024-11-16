#!/usr/bin/node

// Get first argument
const arg = process.argv[2];

// Try to convert the argument into an integer
const num = parseInt(arg);

// Check if the conversion is valid integer
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
