#!/usr/bin/node

counter = 0;
exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter++;
};
