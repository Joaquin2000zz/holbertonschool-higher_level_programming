#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
fs.writeFile(argv[2], argv[3], { encoding: 'utf8', mode: 0o666, flag: 'w+' }, function (err, data) {
  if (err) {
    console.log(err);
  }
});
