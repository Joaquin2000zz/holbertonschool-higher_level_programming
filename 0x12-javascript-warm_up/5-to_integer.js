#!/usr/bin/node

const { argv } = require('process');

if (!isNaN(argv[2])) {
  argv[2] = parseInt(argv[2]);
  process.stdout.write('My number ' + argv[2] + '\n');
} else {
  process.stdout.write('Not a number\n');
}
