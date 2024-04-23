#!/usr/bin/node
const request = require('request');
const process = require('process');
const id = process.argv[2];
const apiEnd = 'https://swapi-api.alx-tools.com/api/films';
request(apiEnd, function (error, response, body) {
  if (error) { console.log(error); } else {
    const films = JSON.parse(body);
    console.log(films.results[id - 1].title);
  }
});
