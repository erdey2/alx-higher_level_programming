#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const process = require('process');
request(process.argv[2], (err, response, body) => {
  if (err) { console.log(err); } else {
    fs.appendFile(process.argv[3], body, 'utf-8',
      function (err) {
        if (err) throw err;
      });
  }
}
);
