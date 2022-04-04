#!/usr/bin/node

const { argv } = require('process');

if (argv[2]) {
  if (!isNaN(argv[2])) {
    argv[2] = parseInt(argv[2]);
    console.log('My number ' + argv[2]);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
