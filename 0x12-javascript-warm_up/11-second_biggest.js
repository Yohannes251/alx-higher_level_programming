#!/usr/bin/node

const len = process.argv.length;
let array;
if (len <= 3) {
  console.log(0);
} else {
  array = process.argv;
  array.slice(2);
  array.sort(function (a, b) { return a - b; });
  console.log(array[array.length - 2]);
}
