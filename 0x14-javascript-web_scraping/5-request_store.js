#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');
const fs = require('fs');
axios.get(argv[2])
  .then(resp => {
    fs.writeFile(argv[3], resp.data, { encoding: 'utf8', mode: 0o666, flag: 'w+' }, function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  });
