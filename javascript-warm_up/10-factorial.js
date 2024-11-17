#!/usr/bin/node

// Function to compute the factorial of a number recursively
function factorial (n) {
  // If n is not a number or less than 0, return 1 (base case)
  if (isNaN(n) || n <= 0) {
    return 1;
  }
  // Recursive case: n * factorial of (n - 1)
  return n * factorial(n - 1);
}

// Get the argument from the command line and cast it to an integer
const arg = parseInt(process.argv[2]);

// Print the result of the factorial computation
console.log(factorial(arg));
