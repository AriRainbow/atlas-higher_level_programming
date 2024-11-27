#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the URL from the command-line arguments
const url = process.argv[2];

// Make a GET request to the specified URL
request(url, (error, response) => {
  if (error) {
    // If an error occurs (e.g., network issue), log the error message
    console.error(`Error: ${error.message}`);
  } else {
    // If no error occurs, log the HTTP status code of the response
    console.log(`code: ${response.statusCode}`);
  }
});
