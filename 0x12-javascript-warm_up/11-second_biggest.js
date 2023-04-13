#!/usr/bin/node
const arglength = process.argv.length;
if (arglength < 4) {
  console.log(0);
} else {
  const myArray = process.argv.sort((x, y) => x - y);
  console.log(myArray[myArray.length - 2]);
}
