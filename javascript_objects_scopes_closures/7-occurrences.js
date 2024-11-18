#!/usr/bin/node

// Function to return the number of occurrences of searchElement in the list
exports.nbOccurences = function (list, searchElement) {
  return list.filter(element => element === searchElement).length;
};
