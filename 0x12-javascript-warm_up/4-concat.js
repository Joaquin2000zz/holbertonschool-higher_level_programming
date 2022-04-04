#!/usr/bin/node

const { argv } = require('process');

if (!argv[2]) {
  process.stdout.write('undefined');
} else {
  process.stdout.write(argv[2]);
}
process.stdout.write(' is ');

if (!argv[3]) {
  process.stdout.write('undefined\n');
} else {
  console.log(argv[3]);
}
