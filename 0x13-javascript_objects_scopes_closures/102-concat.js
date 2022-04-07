#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

if (argv.length === 5) {
  fs.readFile(argv[2], 'utf8', function (err, data) {
    if (err) {
      console.log(err);
    }
    fs.writeFile(argv[4], data, { encoding: 'utf8', flag: 'a+', mode: 0o666 }, (err) => {
      if (err) {
        console.log(err);
      }
    });
  });

  fs.readFile(argv[3], 'utf8', function (err, data) {
    if (err) {
      console.log(err);
    }
    fs.writeFile(argv[4], data, { encoding: 'utf8', flag: 'a+', mode: 0o666 }, (err) => {
      if (err) {
        console.log(err);
      }
    });
  });
}
