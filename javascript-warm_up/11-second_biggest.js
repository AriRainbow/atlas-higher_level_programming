#!/usr/bin/node

// Get arguments from command line (slice to ignore first to elements: node and script name)
const args = process.argv.slice(2).map(Number);

// Check if there are fewer than 2 arguments
if (args.length <= 1) {
  console.log(0);
} else {
  // Sort the arguments in descending order and find the second biggest
  const sortedArgs = args.sort((a, b) => b - a);
  console.log(sortedArgs[1]); // Print second biggest element
}
