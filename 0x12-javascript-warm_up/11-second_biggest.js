#!/usr/bin/node

const { argv } = require('process');

if (!argv[3]) {
  console.log('0');
} else {
  let bigger = 0;
  let second;
  for (let i = 2; argv[i]; i++) {
    if (bigger <= argv[i]) {
      second = bigger;
      bigger = parseInt(argv[i]);
    }
  }
  console.log(second);
}
