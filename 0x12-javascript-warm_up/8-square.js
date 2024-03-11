#!/usr/bin/node
const process = require('node:process');
const args = process.argv;
if (args.length < 3) {
  console.log('Missing size');
}
if (args.length === 3) {
  const number = Number(process.argv[2]);
  if (isNaN(number)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < number; i++) {
      console.log('X'.repeat(number));
    }
  }
}
