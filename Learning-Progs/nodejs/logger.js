const EventEmitter = require('events');
//const emitter = new EventEmitter();

var url = 'https://mylogger.io/log';

class Logger {

    log(message) {
        console.log(message);
        // raised an event
        this.emit('messageLogged',{id: 1, url:'http://'});
    }

}

//log('creation of external module in node.js')

module.exports = log;

//module.exports.message = this.message;
//module.exports.log = log;
//module.exports.endPoint = url;
