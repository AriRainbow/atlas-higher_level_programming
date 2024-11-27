#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

// Validate inputs
if (!url || !filePath) {
  console.log('Usage: ./5-request_store.js <URL> <file path>');
  process.exit(1);
}

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching URL:', error);
    return;
  }

  if (response.statusCode === 200) {
    // Write the response body to the specified file
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  } else {
    console.log(`Failed to fetch URL. HTTP Status Code: ${response.statusCode}`);
  }
});
