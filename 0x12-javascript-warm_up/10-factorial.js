#!/usr/bin/node

const { argv } = require('process');

function rec (a) {
  if (isNaN(a)) {
    return (1);
  }
  if (a === 0) {
    return (1);
  }
  return (rec(a - 1) * a);
}
console.log(rec(parseInt(argv[2])));
