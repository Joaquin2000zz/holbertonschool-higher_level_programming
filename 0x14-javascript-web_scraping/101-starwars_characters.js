#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');
axios.get('https://swapi-api.hbtn.io/api/films/')
  .then(resp => {
    for (let i = 0; resp.data.results[i]; i++) {
      if (resp.data.results[i].episode_id === parseInt(argv[2]))
      {
        for (let j = 0; resp.data.results[i].characters[j]; j++)
        {
          axios.get(resp.data.results[i].characters[j])
            .then(resp => {
              console.log(resp.data.name);
          });
        }
        break;
      }
    }
  });
