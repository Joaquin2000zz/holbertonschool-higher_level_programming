#!/usr/bin/node

const { argv } = require('process');

if (!isNaN(argv[2])) {
  parseInt(argv[2]);
  if (argv[2] > 0) {
    for (let i = 0; i < argv[2]; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurences');
}
