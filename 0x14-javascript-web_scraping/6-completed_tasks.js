#!/usr/bin/node

const argv = process.argv;
const request = require('request');

request(argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const json_body = JSON.parse(body);
    const dict = {};
    for (const i of json_body) {
      if (i.completed === true) {
        if (dict[i.userId] === undefined) {
          dict[i.userId] = 0;
        }
        dict[i.userId] += 1;
      }
    }
    console.log(dict);
  }
});
