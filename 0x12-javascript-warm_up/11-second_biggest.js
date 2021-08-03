#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log('0');
} else {
  const arrayArgs = args.slice(2).map(Number);
  const secondMax = arrayArgs.sort(function (a, b) { return b - a; })[1];
  console.log(secondMax);
}
