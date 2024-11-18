#!/usr/bin/node

// Function to return the reversed version of a list without using reverse()
exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
