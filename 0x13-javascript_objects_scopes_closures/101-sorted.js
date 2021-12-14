#!/usr/bin/node

const dict = require('./101-data').dict;

const dictn = {};
for (const key in dict) {
  if (dictn[dict[key]] === undefined) {
    dictn[dict[key]] = [];
  }
  dictn[dict[key]].push(key);
}
console.log(dictn);
