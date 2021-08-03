#!/usr/bin/node
let itemCounter = 0;
exports.logMe = function (item) {
  console.log(itemCounter + ': ' + item);
  itemCounter++;
};
