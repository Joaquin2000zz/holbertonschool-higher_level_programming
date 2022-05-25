function httpGet(theUrl) {
    let xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.open("GET", theUrl, false); 
    xmlHttpReq.send(null);
    const ret = JSON.parse(xmlHttpReq.responseText);
    return ret['name']
  }
$('header').text(httpGet('https://swapi-api.hbtn.io/api/people/5/?format=json'));