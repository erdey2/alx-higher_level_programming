#!/usr/bin/node
const process = require('node:process');
const args = process.argv;
if (args.length === 3) {
  const number = Number(process.argv[2]);
  if (isNaN(number)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + number);
  }
}
