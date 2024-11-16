#!/usr/bin/node

// Check the number of arguments passed
const argsLength = process.argv.length - 2; // Exclude the first two elements (node and script name)

// Print the corresponding message
if (argsLength === 0) {
  console.log('No argument');
} else if (argsLength === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
