var http = require('http');

http.createServer(function (request, response) {
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.end('Hello there I see you finally got it to work\n');
}).listen(1337);

console.log('Our Glorious server is running at http://127.0.0.1:1337/');