#!/usr/bin/node

const { argv } = require('process');

if (!argv[2]) {
  console.log('No argument');
} else if (argv[2] && !argv[3]) {
  console.log('Argument Found');
} else {
  console.log('Arguments Found');
}
