var fs = require('fs');
var fdr = process.argv[2];
var fdw = process.argv[3];
var len = process.argv[4];

fdr = parseInt(fdr);
fdw = parseInt(fdw);
len = parseInt(len);

var msg = fs.readSync(fdr, len);
fs.writeSync(fdw, msg[0]);
