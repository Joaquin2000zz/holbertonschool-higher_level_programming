#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');

axios.get(argv[2])
  .then(resp => {
    console.log('code: ' + resp.status);
  }).catch(error => {
    console.log('code: ' + error.response.status);
  });
