#!/usr/bin/node
const request = require('request');
const Id = process.argv[2];
const Url = ('https://swapi-api.alx-tools.com/api/films/' + Id);

request(Url, function (error, response, body) {
  if (error) throw error;
  const data = JSON.parse(body);
  console.log(`${data.title}`);
});
