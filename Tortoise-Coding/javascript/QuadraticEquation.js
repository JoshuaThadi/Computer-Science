// program to solve quadratic equation

const readline = require('readline-sync');
let root1, root2;

let a = parseFloat(readline.question('Enter the first number -> '));
let b = parseFloat(readline.question('Enter the second number -> '));
let c = parseFloat(readline.question('Enter the third number -> '));

// calculate discriminant
let discriminant = b * b - 4 * a * c;

// condition for real and different root
if (discriminant > 0) {
  root1 = (-b + Math.sqrt(discriminant)) / (-2 * a);
  root2 = (-b + Math.sqrt(discriminant)) / (2 * a);
  
  console.log(`The roots of quadratic equation are ${root1} and ${root2}`);
}

// condition for real and equal roots 
else if (discriminant = 0) {
  root1 = root2 = -b / (2 * a);

  console.log(`The roots of quadratic equation are ${root1} and ${root2}`);
}

else {
  let realPart = (-b / (2 * a)).toFixed(2);
  let imgPart = (Math.sqrt(-discriminant) / (2 * a)).toFixed(2);

  console.log(`The roots of quadratic equation are ${realPart} + ${imgPart}i and ${realPart} - ${imgPart}i`)
}
