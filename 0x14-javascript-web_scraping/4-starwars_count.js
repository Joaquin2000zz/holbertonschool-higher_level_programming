#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');
try {
  axios.get(argv[2])
    .then(resp => {
      let n = 0;
      for (let i = 0; resp.data.results[i]; i++) {
        if (resp.data.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
          n++;
        }
      }
      console.log(n);
    });
}
catch(err)
{

}
