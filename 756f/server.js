var querystring = require("querystring");
var http = require("http");
var url = require("url");

http.createServer(function(request, response) {
    response.writeHead(200, {"Content-Type":"text/plain"});
    var pathName = url.parse(request.url).pathname;
    var qString = url.parse(request.url).query;
    var a = querystring.parse(qString)['a']
    var b = querystring.parse(qString)['b']

    if(pathName === "/train/plus") {
        response.write((Number(a)*Number(b)).toString());
    }
    response.end()

}).listen(8080)
