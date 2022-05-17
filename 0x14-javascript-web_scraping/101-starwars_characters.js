#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');
axios.get('https://swapi-api.hbtn.io/api/films/' + argv[2] + '/')
  .then(resp => {
    for (let i = 0; resp.data.characters[i]; i++) {
      axios.get(resp.data.characters[i])
        .then(resp => {
          console.log(resp.data.name);
        });
    }
  });
