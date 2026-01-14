const EventEmitter = require('events');
//const emitter = new EventEmitter();

// raised an event
// emitter.emit('messageLogged',{id: 1, url:'http://'});

// raise: logging (data: message)
const Logger = require('./logger');
const logger = new Logger();

//register a listener
logger.on('messageLogged', function(eventArg) {
    console.log('Listened called', eventArg);
});

logger.log('message');