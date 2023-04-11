#!/usr/bin/node
let count = 0;
const num = process.argv[2];
if (isNaN(num)) {
  console.log('Missing number of occurrences');
}

while (count < num) {
  console.log('C is fun');
  count++;
}
