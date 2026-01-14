const readline = require('readline-sync');

const baseValue = parseFloat(readline.question('Enter the base of a triangle -> '));
const heightValue = parseFloat(readline.question('Enter the height of a triangle -> '));

const areaValue = (baseValue * heightValue) / 2;
console.log(`The area of the triangle is ${areaValue}`);

