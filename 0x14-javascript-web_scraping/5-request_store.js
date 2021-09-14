#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');
const request = require('request');

request(argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(argv[3], body, 'utf-8', function (err) {
      if (err) return console.log(err);
    });
  }
});
