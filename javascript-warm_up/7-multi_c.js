#!/usr/bin/node

// Get the first argument passed to the script
const x = parseInt(process.argv[2]);

// Check if the argument is a valid integer
if (isNaN(x)) {
  console.log('Missing number of occurances');
} else {
  // Print "C is fun" x times using a loop
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
