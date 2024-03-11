#!/usr/bin/node
const process = require('node:process');
const args = process.argv;
if (args.length < 3) {
  console.log('No argument');
} else if (args.length === 3) {
  console.log(process.argv[2]);
}
