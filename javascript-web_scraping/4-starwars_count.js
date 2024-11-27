#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const wedgeId = '18'; // Character ID for Wedge Antilles

// Validate the API URL argument
if (!apiUrl) {
  console.log('Please provide the API URL as an argument.');
  process.exit(1);
}

// Make a GET request to the provided API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;

    // Loop through the films to check for Wedge Antilles
    for (const film of films) {
      if (film.characters.some(characterUrl => characterUrl.endsWith(`/${wedgeId}/`))) {
        count++;
      }
    }

    console.log(count);
  } else {
    console.log('Error fetching data:', response.statusCode);
  }
});
