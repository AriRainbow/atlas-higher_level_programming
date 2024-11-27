#!/usr/bin/node

const request = require('request');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];

// Validate input
if (!movieId || isNaN(movieId)) {
  console.log('Please provide a valid movie ID as an argument.');
  process.exit(1);
}

// Make a GET request to the API
request(`${apiUrl}${movieId}/`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log('Error fetching data:', response.statusCode);
  }
});
