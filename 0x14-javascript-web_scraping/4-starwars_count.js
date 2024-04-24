#!/usr/bin/node
const request = require('request');
const process = require('process');
request(process.argv[2], function (error, response, body) {
  if (error) { console.log(error); } else {
    let films = JSON.parse(body).films
    console.log(films.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
