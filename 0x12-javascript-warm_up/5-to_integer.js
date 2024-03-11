#!/usr/bin/node
const process = require('node:process');
let args = process.argv
if (args.length == 3)
{
	let number = Number(process.argv[2]);
	if (number)
	{
		console.log(number);
	}
	else
	{
		console.log('Not a number');
	}
}

