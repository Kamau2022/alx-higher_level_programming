#!/usr/bin/node
const num = process.argv[2];
let n = 0;
let str = '';
if (isNaN(num)) {
  console.log('Missing size');
}

for (let i = 0; i < num; i++) {
  while (n < num) {
    n++;
    str = str + 'X';
  }
  console.log(str);
}
