#!/usr/bin/node

const fs = require('fs');

const firstSource = process.argv[2];
const secondSource = process.argv[3];
const destination = process.argv[4];
const line1 = fs.readFileSync(firstSource, 'utf8');
const line2 = fs.readFileSync(secondSource, 'utf-8');
fs.writeFileSync(destination, line1 + line2);
