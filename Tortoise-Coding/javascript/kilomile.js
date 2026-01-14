// Javascript program to convert kilometers to miles 
const readline = require('readline-sync')

/* Kilometers to miles */
// conversion factor 
const factor = 0.621371;

while(true) {
  try {
    const input = readline.question("Enter the value of kilometers -> ");

    if(input.toLowerCase() === "exit") {
      console.log("Exiting program...");
      break;
    }

    const kilometers = parseFloat(input);
    if(isNaN(kilometers) || kilometers < 0) {
      throw new Error("Invalid input! please enter a valid input");
    }

    const miles = kilometers * factor;
    console.log(`${kilometers} kilometers is equal to ${miles} miles.\n`);

    const input1 = readline.question("Enter the value of miles -> ");
    if(input1.toLowerCase() === "exit") {
      console.log("Exiting program...");
      break;
    }

    const miles1 = parseFloat(input1);
    if(isNaN(miles1) || miles1 < 0) {
      throw new Error("Invalid input! please enter a valid input");
    }

    const kilometers1 = miles1 / factor;
    console.log(`${miles1} miles is equal to ${kilometers1} kilometers.`);
    
  } catch(error) {
    console.log(error.message);
  }
}

