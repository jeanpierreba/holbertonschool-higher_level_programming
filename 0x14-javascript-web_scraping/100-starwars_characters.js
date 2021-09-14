#!/usr/bin/node

const argv = process.argv;
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  }
  JSON.parse(body).characters.forEach(function (url, callback) {
    request(url, function (error, response, body) {
      if (error) {
        console.error(error)
      }
      console.log(JSON.parse(body).name);
    });
  });
});
