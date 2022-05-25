function httpGet(theUrl) {
    let xmlHttpReq = new XMLHttpRequest();
    xmlHttpReq.open("GET", theUrl, false); 
    xmlHttpReq.send(null);
    const Dict = JSON.parse(xmlHttpReq.responseText);
    let List = []
    const results = Dict['results']
    for (let i = 0; results[i]; i++) {
      List.push(results[i]['title'])
    }
    return List
  }
const List = httpGet('https://swapi-api.hbtn.io/api/films/?format=json')
for (var i = 0; List[i]; i++) {
    $('UL#list_movies').append("<li>" + List[i]);
}