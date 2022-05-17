#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');
axios.get('https://swapi-api.hbtn.io/api/films/' + argv[2] + '/')
  .then(resp => {
    console.log(resp.data.title);
  });
