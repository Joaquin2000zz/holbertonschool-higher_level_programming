#!/usr/bin/node

const { argv } = require('process');

if (!argv[3]) {
  console.log('0');
} else {
  const list = [];
  for (let i = 2; argv[i]; i++) {
    list.push(parseInt(argv[i]));
  }
  const sorted = list.sort((f, s) => s - f);
  console.log(sorted[1]);
}
