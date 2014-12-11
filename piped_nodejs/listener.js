var net = require('net'),
    fs = require('fs');


var run = function(unix_sock) {
    var server = net.createServer(),
        full_data = 'echo: ';

    server.on('listening', function() {
        console.log('listening on: '+server.address());
    });
    server.on('connection', function(connection) {
        console.log('connected');
        connection.on('data', function (data) {
            console.log(data.length);
            full_data += data;
            connection.write(full_data);
        });
        connection.on('end', function () {
            console.log('connection ended');
        });
        connection.on('error', function(error) {
            console.log(error);
        });
        connection.on('close', function() {
           console.log('connection closed');
        });
    });
    server.on('error', function(error) {
       console.log(error);
    });
    server.on('close', function() {
        console.log('listener closed');
    });
    server.listen(unix_sock)
};


unix_sock = process.argv[2];
run(unix_sock);