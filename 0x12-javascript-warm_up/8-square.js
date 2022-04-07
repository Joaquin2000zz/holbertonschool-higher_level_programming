#!/usr/bin/node

const { argv } = require('process');

if (!isNaN(argv[2])) {
  argv[2] = parseInt(argv[2]);
  if (argv[2] > 0) {
    const print = 'X'.repeat(argv[2]);
    for (let i = 0; i < argv[2]; i++) {
      console.log(print);
    }
  }
} else {
  console.log('Missing size');
}
