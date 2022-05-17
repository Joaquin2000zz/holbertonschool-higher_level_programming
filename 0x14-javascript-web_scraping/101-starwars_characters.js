#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');
axios.get('https://swapi-api.hbtn.io/api/films/')
  .then(resp => {
    argv[2] = parseInt(argv[2]);
    if (argv[2] >= 4) {
      argv[2] -= 3;
    } else {
      argv[2] += 3;
    }
    for (let i = 0; resp.data.results[i]; i++) {
      if (resp.data.results[i].episode_id === argv[2]) {
        for (let j = 0; resp.data.results[i].characters[j]; j++) {
          axios.get(resp.data.results[i].characters[j])
            .then(resp => {
              console.log(resp.data.name);
            });
        }
        break;
      }
    }
  });
