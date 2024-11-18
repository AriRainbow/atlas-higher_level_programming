#!/usr/bin/node

// Function to return a converter function for a given base
exports.converter = function (base) {
  return function (num) {
    return num.toString(base); // Convert the number from base 10 to the specified base
  };
};
