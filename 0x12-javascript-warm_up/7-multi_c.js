#!/usr/bin/node

let i = 0;
let j;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  j = parseInt(process.argv[2]);
  while (i < j) {
    console.log('C is fun');
    i++;
  }
}
