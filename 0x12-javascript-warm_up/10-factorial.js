#!/usr/bin/node
function factorial (num) {
  if (!num) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const num = process.argv[2];
console.log(factorial(num));
