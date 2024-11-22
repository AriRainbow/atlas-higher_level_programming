#!/usr/bin/node

const fs = require('fs');
// Get file path from command line arguments
const filePath = process.argv[2];

// Try to read the fie content
try {
  const content = fs.readFileSync(filePath, 'utf8');
  console.log(content); // Print content if file reading succeeds
} catch (error) {
  console.error(error); // Print error object if reading file fails
}
