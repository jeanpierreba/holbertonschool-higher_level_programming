#!/usr/bin/node
const args = process.argv;
const x = parseInt(args[2]);
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}
