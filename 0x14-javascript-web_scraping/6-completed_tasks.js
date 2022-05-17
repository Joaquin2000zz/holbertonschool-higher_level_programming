#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');
axios.get(argv[2])
  .then(resp => {
    const dict = {};
    let n = 0;
    for (let i = 0; resp.data[i]; i++) {
      if (i !== 0) {
        if (resp.data[i].userId !== resp.data[i - 1].userId) {
          n = 0;
        }
      }
      if (resp.data[i].completed === true) {
        dict[resp.data[i].userId] = ++n;
      }
    }
    console.log(dict);
  });
