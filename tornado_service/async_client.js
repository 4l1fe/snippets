var http = require('http');


for (var i=0;i<1;i++) {
    console.log(i.toString());
    var request = http.get("http://127.0.0.1:8888/?idx="+i, function(res) {
        console.log("Got response: " + res.statusCode);
        res.on('error', function(e) {console.log("Got error: " + e.message);});
        res.on('data', function(data) {console.log(data)});
    });
    request.on("error", function(error) {
        console.log("request error: "+error.message);
    });
    request.end();
}
