#!/usr/bin/node
var arguments = process.argv;
const fs = require('fs');
fs.readFile(arguments[2], 'utf-8', (err, data) => {
    if (err) throw err;
    console.log(data);
})
