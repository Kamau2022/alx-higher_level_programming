#!/usr/bin/node

let request = require('request');

request.get(
    process.argv[2],
    function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(response);
        }
    }
);


