#!/usr/bin/node
const dict = require('./101-data').dict;
const newKey = [];
const newDict = {};
let i = 0;
for (const [key, value] of Object.entries(dict)) {
  if (!newKey.includes(value)) {
    newKey.push(value);
    newDict[newKey[i]] = [key];
    i++;
  } else {
    for (let j = 0; newKey[j]; j++) {
      if (newKey[j] === value) {
        newDict[newKey[j]].push(key);
      }
    }
  }
}
console.log(newDict);
