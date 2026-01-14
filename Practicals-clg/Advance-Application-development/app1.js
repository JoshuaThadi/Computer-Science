// WAP to implement error handling in angular.js

const readline = require('readline-sync');

const operator = readline.question("Enter operator [+, -, *, /] -> ");
const num1 = parseFloat(readline.question("Enter a number -> "));
const num2 = parseFloat(readline.question("Enter another number -> "));

let result;
switch (operator) {
    case "+":
        result = num1 + num2;
        console.log(`Addition of ${num1} & ${num2} is ${result}`);
        break;
    case "-":
        result = num1 - num2;
        console.log(`Subtraction of ${num1} & ${num2} is ${result}`);
        break;
    case "*":
        result = num1 * num2;
        console.log(`Multiplication of ${num1} & ${num2} is ${result}`);
        break;
    case "/":
        if (num2 !== 0) {
            result = num1 / num2;
            console.log(`Division of ${num1} & ${num2} is ${result}`);
        } else {
            console.log("Error: Division by zero is not allowed.");
        }
        break;
    default:
        console.log("Invalid operator");
}
