#!/usr/bin/node
const process = require('node:process');
const msg = 'C is fun';
const args = process.argv;
if (args.length < 3) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(msg);
  }
}
