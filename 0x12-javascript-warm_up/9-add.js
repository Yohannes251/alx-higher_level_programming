#!/usr/bin/node

function add (a, b) {
  let sum;
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    sum = a + b;
    console.log(sum);
  }
}
add(parseInt(process.argv[2]), parseInt(process.argv[3]));
