#!/usr/bin/node
let args = process.argv;
if (isNaN(args[2])) {
	console.log("Not a number");
} else {
	console.log("my number: " + parseInt(args[2]));
}
