#!/usr/bin/node
const process = require('node:process');
const args = process.argv;
if (args.length === 3) {
  const number = Number(process.argv[2]);
  if (number) {
    console.log(number);
  } else {
    console.log('Not a number');
  }
}
