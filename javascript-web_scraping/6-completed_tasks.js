#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

// Validate the input
if (!apiUrl) {
  console.log('Usage: ./6-completed_tasks.js <API URL>');
  process.exit(1);
}

// Make a GET request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const userTaskCount = {};

    // Loop through the tasks and count completed tasks by user id
    tasks.forEach(task => {
      if (task.completed) {
        if (userTaskCount[task.userId]) {
          userTaskCount[task.userId]++;
        } else {
          userTaskCount[task.userId] = 1;
        }
      }
    });

    // Print users with completed tasks
    console.log(userTaskCount);
  } else {
    console.log('Error fetching data:', response.statusCode);
  }
});
