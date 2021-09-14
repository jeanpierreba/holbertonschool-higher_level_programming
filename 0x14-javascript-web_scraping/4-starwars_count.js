#!/usr/bin/node

const argv = process.argv;
const request = require('request');

request(argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const json_body = JSON.parse(body);
    let count = 0;
    for (const i of json_body.results) {
      for (const j of i.characters) {
        if (j.search(id) > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
