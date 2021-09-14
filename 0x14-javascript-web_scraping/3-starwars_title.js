#!/usr/bin/node

const argv = process.argv;
const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + argv[2], function (error, response, body) {
  if (error === null) {
    const json_body = JSON.parse(body);
    console.log(json_body.title)
  } else {
    console.log(error)
  }
});
