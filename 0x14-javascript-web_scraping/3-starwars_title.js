#!/usr/bin/node

const argv = process.argv;
const request = require('request');

request('http://swapi.co/api/films/' + argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
