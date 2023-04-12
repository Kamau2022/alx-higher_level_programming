#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
const newObject = {
  type: 'object',
  value: 89
};
myObject.value = newObject.value;
console.log(myObject);
