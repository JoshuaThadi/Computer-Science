// file system module
const fs = require('fs');

var files = fs.readdirSync('./');
console.log(files);

// Error handling
fs.readdir('./', function(err, files) {

    if(err) console.log('Error', err);
    else console.log('Results', files);

});

fs.readdir('$', function(err, files) {

    if(err) console.log('Error', err);
    else console.log('Results', files);

});