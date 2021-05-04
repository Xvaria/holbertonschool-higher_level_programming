#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const argv = process.argv;

request(argv[2], function (error, response) {
  if (error) {
    return console.error(error);
  }
  fs.writeFile(argv[3], response.body, function (error) {
    if (error) throw error;
  });
});
