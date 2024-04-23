#!/usr/bin/node
const request = require('request');
const process = require('process');
const apiEnd = 'https://swapi-api.alx-tools.com/api/people/18';
request(apiEnd, function (error, response, body) {
  if (error) { console.log(error); } else {
    const films = JSON.parse(body);
    console.log(films.films.length);
  }
});
