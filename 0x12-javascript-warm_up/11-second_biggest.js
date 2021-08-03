#!/usr/bin/node
let args = process.argv;
if (args.length <= 3) {
	console.log("0");
} else {
	const array_args = args.slice(2).map(Number);
	const second_max = array_args.sort(function (a, b) { return b - a; })[1];
	console.log(second_max);
}
