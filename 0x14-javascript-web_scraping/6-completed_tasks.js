#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');
axios.get(argv[2])
  .then(resp => {
    const dict = {};
    for (let i = 0; resp.data[i]; i++) {
      if (resp.data[i].completed === true) {
        if (isNaN(dict[resp.data[i].userId])) {
          dict[resp.data[i].userId] = 1;
        } else {
          dict[resp.data[i].userId] += 1;
        }
      }
    }
    console.log(dict);
  });
