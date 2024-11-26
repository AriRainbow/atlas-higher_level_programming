#!/usr/bin/node

// Import the 'fs' module to work with the filesystem
const fs = require('fs');

// Get the file path from the first command line argument
const filePath = process.argv[2];

// Get the string content to write from the second command line argument
const content = process.argv[3];

try {
  // Attempt to write the content to the specified file
  // The 'writeFileSync' method writes the file synchronously in utf-8 encoding by default
  fs.writeFileSync(filePath, content);
  // If the write operation succeeds, log a success message
  console.log('String written to file successfully.');
} catch (error) {
  // If an error occurs during the write operation, log the error object 
  console.error(error);
}
