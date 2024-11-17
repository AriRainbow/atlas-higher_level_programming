#!/usr/bin/node

// Get the first argument passed to the script
const size = parseInt(process.argv[2]);

// Check if the argument is a valid integer
if (isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  // Print the square of 'X' characters
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
