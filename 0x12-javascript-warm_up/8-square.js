#!/usr/bin/node

let i = 0;
let j;
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  j = parseInt(process.argv[2]);
  while (i < j) {
    console.log('X'.repeat(j));
    i++;
  }
}
