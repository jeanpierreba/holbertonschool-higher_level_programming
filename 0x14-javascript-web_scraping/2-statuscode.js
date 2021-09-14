#!/usr/bin/node

const argv = process.argv;
const request = require('request');

request(argv[2], function (error, response) {
  if (error) {
    console.error(error);
  }
  console.log('code:', response && response.statusCode);
});
