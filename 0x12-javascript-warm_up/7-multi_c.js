#!/usr/bin/node
let args = process.argv;
let x = parseInt(args[2]);
if (isNaN(x)) {
	console.log("Missing number of occurrences");
} else {
	for (let i = 0; i < x; i++) {
		console.log("C is fun");
	}
}
