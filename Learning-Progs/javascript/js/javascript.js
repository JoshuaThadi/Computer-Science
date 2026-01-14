// 1] in-line comment
console.log("Hello world"); // this is inline comment

// multi-line comment 
/* var number = 5;
var num = 6;
if (num == number) {
    console.log('True');
} else {
    console.log('False');
} */ 


/* 2]  Data types and variables
    undefined, null, boolean, string, symbol, number and object
*/
var name = 'Josh';
let myName = 'JoJo';
const pi = 3.14;


// 3] Storing Values with Assignment Operators
var a;
var b = 2;
console.log(a);

a = 7;
b = a;
console.log(b);


// 3.1] Initializing values with assignment operators
var a = 9;


// 4] Case Sensitive in variable
    
    // declaration
    var studlyCapVar;
    var properCamelCase;
    var titleCaseOver;

    // assignments
    studlyCapVar = 19;
    properCamelCase = 10;
    titleCaseOver = 30;
    

// 5] Compound Assignment with Augmentation
a = a * 5;
a *= 5; // augmented


// 6] Escaping literals Quotes
var myStr = "I am a \"double quoted\" string inside a \"double quotes\". ";
console.log(myStr);

// concatenating string
var ourStr = 'I come first.\t' + "This is the end."
console.log(ourStr)

var myStr = 'I come first. ';
myStr = myStr + 'I come second.';
console.log(myStr);

// constructing with strings
var ourStr = 'we are free';
var myStr = 'Are you Free? ' + ourStr + " Yes for sure";
console.log(myStr)

// Bracket Notation to find first characters in string
var firstLetterOfFirstName = "";
var firstName = "Ada";
firstLetterOfFirstName = firstName[0];
console.log(firstLetterOfFirstName);

// Bracket Notation to find Nth-to-last character in string
var lastName = "LoveLace";
var secondLastLetterOfLastName = lastName[lastName.length - 2];
console.log(secondLastLetterOfLastName)


// 8] Word Blanks
function wordBlanks(myNoun, myAdjective, myVerb, myAdverb) {
    var result = "";
    result += "The " + myAdjective + " " + myNoun + " " + myVerb + " to the store " + myAdverb;
    return result;
}
console.log(wordBlanks("dog", "big", "ran", "quickly"));


// 9] Store multiple values in array

/* In JavaScript, "Word Blanks" refers to a programming exercise or challenge, often inspired by the game Mad Libs. The core concept involves constructing a complete sentence by filling in missing words (like nouns, verbs, adjectives, and adverbs) into a pre-defined sentence structure. */

var myArray = ["John", 23];
console.log(myArray);


// 10] Nested Arrays

/* A nested array is an array that contains one or more other arrays as its elements. This creates a hierarchical or multi-dimensional data structure, where an "outer" or "parent" array holds "inner" or "child" arrays. */

var ourArray = [["My Universe", 777], ["Everything", 1111]];
console.log(ourArray);


// 11] Access array data with indexes
var myArray = [50, 60, 70];
var myArray = myArray[1];
console.log(myArray);


// 12] Modify array data with indexes
var ourArray = [19, 65, 99];
ourArray[1] = 45;
console.log(ourArray);


// 13] Access multi-dimensional array with indexes
var myArray = [[1, 2, 3], [4, 5, 6], [[7, 8, 9], [10, 11]]];
var myData = myArray[2][0][0];
console.log(myData);


// 14] Manipulate Arrays with push() function
/* push() - adds an item to the end. */

var myArray = ["Josh", "Boss"];
myArray.push(["John", "doe"]);
console.log(myArray);


// 15] Manipulate Arrays with pop() function
/* pop() - takes the last item off. . */

var myArray = [["John", 23], ["Joe", 34]];
myArray.pop();
console.log(myArray);


// 16] Manipulate arrays with shift()
/* shift() - removes the first item. */

var ourArray = ["simpson", "J", ["cat"]];
var removedFromOurArray = ourArray.shift();
console.log(removedFromOurArray, ourArray);


// 17] Manipulate arrays with unshift()
/* unshift() - puts an item at the start.  */

var ourArray = ["simpson", "J", ["cat"]];
ourArray.unshift("Happy");
console.log(ourArray);


// 18] Shopping List
var myList = [["cereal", 3], ["milk", 2], ["eggs", 6]];
console.log(myList);


// 19] Write reusable code with functions
function ourReusableFunction() {
    console.log("Hello World!");
}
ourReusableFunction();
ourReusableFunction();
ourReusableFunction();


// 20] Passing values to the functions and arguments
function ourFunctionWithArgs(a, b) {
    console.log(a - b);
}
ourFunctionWithArgs(10, 5);


// 21] Global scope and functions
var myGlobal = 10;

function funcOne() {
    var oopsGlobal = 5;
}

function funcTwo() {
    var output = "";
    if (typeof myGlobal != "undefined") {
        output += "myGlobal: " + myGlobal;
    }
    if (typeof oopsGlobal != "undefined") {
        output += " oopsGlobal: " + oopsGlobal;
    }
    console.log(output);
}

funcOne();
funcTwo();


// 22] Local scope and function
function localScopeFun() {
    var myVar = 75;
    console.log(myVar);
}
localScopeFun();


// 23] Global vs local scope in functions
var outerWear = "T-shirt";
function myOutFit() {
    var outerWear = "Sweater";
    return outerWear;
}
console.log(myOutFit());
console.log(outerWear);


// 24] Assignment with the returned value
var changed = 0
function change(num) {
    return (num + 5) / 7;
}
changed = change(10);
console.log(changed);


// 25] Stand In Line

/* The JSON.stringify() method in JavaScript converts a JavaScript value (usually an object or array) into a JSON (JavaScript Object Notation) string. This process is known as serialization. */

function nextInLine(arr, item) {
    arr.push(item);
    return arr.shift();
}

var testArr = [1, 2, 3, 4, 5];
console.log("Before -> " + JSON.stringify(testArr));
console.log(nextInLine(testArr, 6));
console.log("After -> " + JSON.stringify(testArr));


// 26] Boolean Values

/* In JavaScript, a Boolean is a primitive data type that represents a logical entity and can only have one of two values: true or false. */

function welcomeTooBoolean() {
    return true;
}


// 27] use conditional Logic with if statements
function ourTrueOrFalse(ourIsTrue) {
    if (ourIsTrue) {
        return "Yes, It is true!";
    }
    return "No, It is False"
}
console.log(ourTrueOrFalse(true));


// 28] Comparison with the strict equality operator
function testStrict(val) {
    if (val === "7") {
        return "It is equal.";
    }
    return "Not equal.";
}
console.log(testStrict(7));


// 29] Comparison with the Logical And Operator
function testLogicalAnd(val) {
    if (val <= 25 && val >= 15) {
        return true;
    }
    return false;
}
console.log(testLogicalAnd(23));


// 30] comparison with Logical Or operator
function testLogicalOr(val) {
    if (val < 10 || val > 20){
        return "Outside";
    }
    return "Inside";
}
console.log(testLogicalOr(15));


// 31] Else statement

/* In JavaScript, the else statement is a control flow statement used in conjunction with the if statement. It provides an alternative block of code to be executed when the condition specified in the preceding if statement evaluates to false.  */

function testElse(val) {
    var result = "";
    if (val > 5) {
        result = "Value is big";
    } else {
        result = "Value is small";
    }
    return result;
}
console.log(testElse(10));


// 32] Else if statement

/* The else if statement in JavaScript is a conditional control structure that allows for the evaluation of multiple conditions in a sequential manner. It is used when there are more than two possible outcomes based on different conditions. */

function testElseIf(val) {
    if (val > 10) {
        return "value is bigger than 10";
    } else if (val < 5) {
        return "value is smaller than 5";
    } else {
        return "value is in between 5 and 10";
    }
}
console.log(testElseIf(9));


// 33] Golf Code

/* "Code Golf" in JavaScript, or any programming language, refers to the practice of solving a given programming problem using the shortest possible code, measured in the number of characters.  */

/* 

Strokes      Return
1            "Hole-in-one!"
<= par - 2   "Eagle"
par - 1      "Birdle"
par          "Par"
par + 1      "Bogey"
par + 2      "Double Bogey"
>= par + 3   "Go Home!"

*/

var names = ["Hole-in-one!", "Eagle", "Birdle", "Par", "Bogey", "Double Bogey", "Go Home!"];

function golfCode(par, strokes) {
    if (strokes == 1) {
        return names[1];
    } else if (strokes <= par - 2) {
        return names[2];
    } else if (strokes == par) {
        return names[3];
    } else if (strokes == par + 1) {
        return names[4];
    } else if (strokes == par - 2) {
        return names[5];
    } else if (strokes >= par - 2) {
        return names[6];
    }
}
console.log(golfCode(5, 8))


// 34] Switch Statements
/* A switch statement is a control flow statement that allows a variable to be tested against a list of values.  */

function caseInSwitch(val) {
    var answer = "";
    switch(val) {
        case 1:
            answer = "Alpha";
            break;
        case 2:
            answer = "Beta";
            break;
        case 3:
            answer = "Gamma";
            break;
        case 4:
            answer = "Delta";
            break;
    }
    return answer;
}
console.log(caseInSwitch(2));


// 35] Multiple Identical options in switch statements
function sequentialSizes(val) {
    var answer = ""
    switch(val) {
        case 1:
        case 2:
        case 3:
            answer = "low";
            break;
        case 4:
        case 5:
        case 6:
            answer = "mid";
            break;
        case 7:
        case 8:
        case 9:
            answer = "high";
            break;
    }
    return answer;
}
console.log(sequentialSizes(4));


// 36] Returning early patterns from function
function abTest(a, b) {
    if (a < 0 || b < 0) {
        return undefined;
    }
    return Math.round(Math.pow(Math.sqrt(a) + Math.sqrt(b), 2));
}
console.log(abTest(3, 3));


// 37] Javascript Objects

/* In JavaScript, an object is a complex data type that allows for the storage and organization of data in a structured manner. Objects are fundamental to JavaScript and are used to represent real-world entities or concepts within a program.  */

var ourDog = {
    "name": "Camper",
    "legs": 4,
    "tails": 1,
    "friends":  ["everything!"]
};
console.log(ourDog);


// 38] Accessing Object properties with Dot notation
var testObj = {
    "hat" : "ballcap",
    "shirt" : "jersey",
    "shoes" : "cleats"
}; console.log(testObj);

var hatValue = testObj.hat;
var shirtValue = testObj.shirt;
var shoesValue = testObj.shoes;

console.log(hatValue);
console.log(shirtValue);
console.log(shoesValue);


// 39] Accessing Object properties with bracket notation

/* Bracket notation (square brackets []) is used in JavaScript objects for property access and assignment in situations where dot notation (.) is not suitable or possible. */

var testObj = {
    "an entree" : "hamburger",
    "my side" : "veggies",
    "the drink" : "water"
}; console.log(testObj);

var entreeValue = testObj["an entree"];
var sideValue = testObj["my side"];
var drinkValue = testObj["the drink"];

console.log(entreeValue);
console.log(sideValue);
console.log(drinkValue);


// 40] Accessing object properties with variables
var testObj = {
    12 : "Natanya",
    13 : "Donald",
    14 : "Putin"
}; console.log(testObj);

var playerNumberOne = 12;
var playerOne = testObj[playerNumberOne];
var playerNumberTwo = 13;
var playerTwo = testObj[playerNumberTwo];
var playerNumberThree = 14;
var playerThree = testObj[playerNumberThree];

console.log(playerOne);
console.log(playerTwo);
console.log(playerThree);


// 41] Updating Object properties
var myDog = {
    "name" : "Coder",
    "legs" : 4,
    "tails" : 1,
    "friends" : ["FreeCodeCamp Camper"]
}; console.log(myDog.name);

myDog.name = "Happy Coder";
console.log(myDog.name);


// 42] Add new properties to an object
var myDog = {
    "bark" : "wowh",
    "legs" : 4,
    "tails" : 1,
    "friends" : ["FreeCodeCamp Camper"]
}; console.log(myDog.bark);

myDog["bark"] = "bow-wow";
console.log(myDog["bark"]);


// 43] delete properties from an object
var myDog = {
    "name" : "camper",
    "legs" : 4,
    "tails" : 1,
    "friends" : ["FreeCodeCamp Camper"],
    "bark" : "wowh",
}; console.log(myDog);

delete myDog.bark;
console.log(myDog);


// 44] Using Objects for lookups
function phoneticLookup(val) {
    var result = "";
    var lookup = {
        "alpha" : "Adams",
        "bravo" : "Boston",
        "charlie" : "chicago",
    };
    result = lookup[val];
    return result;
};
console.log(phoneticLookup("charlie"));


// 45] Testing objects for properties
var myObj = {
    gift : "pony",
    pet : "kitten",
    bed : "sleigh",
};
function checkObj(checkProp) {
    var hasOwnProperty;
    if (myObj.hasOwnProperty(checkProp)) {
        return myObj[checkProp];
    } else {
        return "Property not found";
    }
};
console.log(checkObj("gift"));


// 46] Accessing Nested Objects
var myStorage = {
    "car" : {
        "inside" : {
            "glove box" : "maps",
            "passenger seat" : "crumbs",
        },
        "outside" : {
            "trunk" : "jack",
        }
    }
};
var gloveBoxContents = myStorage.car.inside["glove box"];
console.log(gloveBoxContents);


// 47] Accessing nested arrays
var ourPlants = [
    {
        type: "flowers", 
        list : ["rose", "tulip", "dandelion"]
    },
    {
        type: "trees", 
        list: ["fir", "pine", "birch"]
    }
];

var secondTree = ourPlants[1].list[1];
console.log(secondTree);


// 48] Record Collection
/* JSON.parse() is a built-in JavaScript method used to convert a JSON-formatted string into a JavaScript object. This process is known as "parsing" JSON. */

var collection = {
    "2548" : {
        "album" : "Slippery When Wet",
        "artist" : "Bon Jovi",
        "tracks" : [
            "Let it rock",
            "You Give love a bad name"
        ]
    },
    "2468" : {
        "album" : "1999",
        "artist" : "Prince",
        "tracks" : [
            "1999",
            "Little Red Corvette"
        ]
    },
    "1245" : {
        "album" : "Robert Palmet",
        "tracks" : []
    },
    "5439" : {
        "album" : "ABBA Gold",
    },
};

var collectionCopy = JSON.parse(JSON.stringify(collection));
function updateRecords(id, prop, value) {
    
    if (value === "") {
        delete collection[id][prop]; // delete if the value is blank
    } else if (prop === "tracks") {
        collection[id][prop] = collection[id][prop] || [];// pass the same track if exists or let it be empty
        collection[id][prop].push(value); // push the value if changed
    } else {
        collection[id][prop] = value; // let the previous value be like that.
    }
    
    return collection;
};

console.log(updateRecords(1245, "album", "Cole Palmer"));


// 49] Iterative with while loops
var myArray = [];
var i = 0;
while (i < 5) {
    myArray.push(i);
    i++;
};
console.log(myArray);


// 50] Iterative with for loop
var ourArray = [];
for (var i = 0; i < 5; i++) {
    ourArray.push(i);
};
console.log(ourArray);


// 51] Count Backwards through for loops
var ourArray = [];
for (var i = 10; i > 0; i -= 1) {
    ourArray.push(i);
};
console.log(ourArray);


// 52] Iterate through an array with a for loop
var ourArr = [9, 10, 11, 12];
var ourTotal = 0;
for (var i = 0; i < ourArr.length; i++) {
    ourTotal = ourTotal + ourArr[i];
};
console.log(ourTotal);


// 53] Nesting For Loops
function multiplyAll(arr) {
    var product = 1;
    for (var i = 0; i < arr.length; i++) {
        for (var j = 0; j < arr[i].length; j++) {
            product = product * arr[i][j];
        }
    }
    return product;
};

var product = multiplyAll([[1, 2], [3, 4], [5, 6, 7]]);
console.log(product);


// 54] Iterate with do while loop
var Array = [];
var i = 10;
do {
    Array.push(i);
    i++;
} while (i < 5)

console.log(i, Array);


// 55] Profile Lookup - coding challenge
var contacts = [
    {
        "firstName" : "Harry",
        "lastName" : "Potter",
        "number" : "0994372684",
        "likes" : ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName" : "Sherlock",
        "lastName" : "Holmes",
        "number" : "unknown",
        "likes" : ["Intriguing cases", "Violin"]
    },
];

function lookUpProfile(name, prop) {

    for (var i = 0; i < contacts.length; i++){
        if (contacts[i].firstName === name){
            return contacts[i][prop] || "No such property";
        }
    }
    return "No such contacts";
};

var data = lookUpProfile("Harry", "likes");
console.log(data);


// 56] Generate Random factors
function randomFraction() {
    return Math.random();
};
console.log(randomFraction());


// 57] Generate Random whole number
function randomWholeNumber() {
    return Math.floor(Math.random() * 10);
};
console.log(randomWholeNumber());


// 58] Generate random whole number within a range
function randomWholeNumber1(ourMin, ourMax) {
    return Math.floor(Math.random() * (ourMax - ourMin + 1)) + ourMin;
};
console.log(randomWholeNumber1(1, 9));


// 59] use the parseInt function

/* parseInt() in JavaScript is a global function used to parse a string argument and convert it into an integer. It is commonly used when you need to perform mathematical operations on values that are initially represented as strings. 
 */

function convertToInteger(str) {
    return parseInt(str);
};
var parseIntToString = convertToInteger("56");
console.log(parseIntToString);


// 60] Use the parseInt function with a Radix

/*  The radix parameter in parseInt() specifies the base of the numeral system to be used when parsing the string. 
 radix: An optional integer between 2 and 36 (inclusive) that represents the base of the numeral system of the string.*/

function convertToIntegerBaseTwo(str) {
    return parseInt(str, 2);
};
var parseIntRadixBaseTwo = convertToIntegerBaseTwo("10011");
console.log(parseIntRadixBaseTwo);


// 61] Use the conditional ternary operator

/* The ternary operator in JavaScript, also known as the conditional operator, is a concise way to write conditional expressions. It is a single-line alternative to a simple if...else statement.  */

const checkEvenOdd = (number) => {
    return number % 2 === 0 ? "Even" : "Odd";
};
console.log(checkEvenOdd(10));


// 62] Use multiple conditional (ternary) operators
function constMultipleTernaryOperator(number) {
    return number > 0 ? "Positive" : number < 0 ? "Negative" : "Zero";
};
var ternaryOperatorPositive = constMultipleTernaryOperator(10);
var ternaryOperatorNegative = constMultipleTernaryOperator(-10);
var ternaryOperatorNull = constMultipleTernaryOperator(0);
console.log(ternaryOperatorPositive);
console.log(ternaryOperatorNegative);
console.log(ternaryOperatorNull);


// 63] Use Strict

/* The "use strict" directive in JavaScript enables strict mode for the code. Strict mode introduces a more restrictive and secure environment for JavaScript execution, enforcing better coding practices and eliminating some problematic or confusing features of the language. */
function catTalk(prop) {
    "use strict";
    var catName = prop;
    catName = catName + " says meow";
    return catName;
};
console.log(catTalk("stuart"));


// 64] Mutate an array declared with const
const s = [5, 7, 9];
console.log(s);
function editInPlace() {
    s[0] = 1;
    s[1] = 2;
    s[2] = 3;
};
editInPlace();
console.log(s)


// 65] Prevent object mutation

/* Object.freeze() in JavaScript is a method that makes an object immutable. Once an object is frozen, its properties cannot be modified, added, or deleted. This effectively makes the object read-only at its top level.  */

/* A try and catch block is a fundamental construct in many programming languages used for exception handling. This mechanism allows programs to gracefully manage errors and unexpected situations that may arise during execution, preventing abrupt termination. */

function objectFreeze() {
    "use strict";
    const MATH_CONSTANT = {
        PI : 3.14
    };

    Object.freeze(MATH_CONSTANT);

    try {
        MATH_CONSTANT.PI = 99;
    } catch (error) {
        console.log("There is an error, because object.freeze prevent object mutation\n", error);
    }
    return MATH_CONSTANT.PI;
};
const PI = objectFreeze();
console.log("------------------------")
console.log(PI, "is the object value");


// 66] Arrow function

/* An arrow function in JavaScript is a concise syntax for writing anonymous function expressions, introduced in ECMAScript 6 (ES6). It provides a more compact and readable way to define functions compared to traditional function expressions. */
const magic = () => new Date();
console.log(Date());


// 67] Arrow function with parameters

/* The concat() function concatenates the string arguments to the calling string and returns a new string. If the arguments are not of the type string, they are converted to string values before concatenating.1 */
const myConcat = (arrOne, arrTwo) => arrOne.concat(arrTwo);
console.log(myConcat([1, 2], [3, 4, 5]));


// 68] Higher Order Arrow function

/* A callback function in JavaScript is a function that is passed as an argument to another function, with the intention of being executed at a later time. This "later time" often refers to the completion of an asynchronous operation or a specific event.  */

/* The .filter() method is a common array method in many programming languages, particularly in JavaScript. Its primary function is to create a new array containing only the elements from the original array that satisfy a specified condition. */

/* The Number.isInteger() method in JavaScript is a static method used to determine whether a given value is an integer. */

// part - 1
const realNumberArray = [4, 5.6, -9.8, 3.14, 42, 6, 8.34, -2];
const squareList = (arr) => {
    const squaredIntegers = arr.filter(num => Number.isInteger(num) && num > 0).map(x => x * x);
    return squaredIntegers;
};
const squaredIntegers = squareList(realNumberArray);
console.log(squaredIntegers);

// part - 2
const increment = (function() {
    return function increment(number, value = 1) {
        return number + value;
    };
}) ();
console.log(increment(10, 2));
console.log(increment(10));


// 69] Rest operator with function parameters

/* The rest operator in JavaScript, denoted by three consecutive dots (...), is a feature introduced in ES6 (ECMAScript 2015) that allows you to collect an indefinite number of elements into an array. It is primarily used in two contexts: Function Parameters (Rest Parameters).  */

/* The .reduce() method in JavaScript is a higher-order array method that iterates over each element of an array and applies a "reducer" callback function to accumulate a single value. This single value can be a number, a string, an object, or any other data type.  */

const sum = (function() {
    return function sum(...args) {
        return args.reduce((a, b) => a + b, 0);
    };
}) ();
console.log(sum(1, 2, 3, 4, 5));


// 70] Spread operator to evaluate arrays In-place

/* The spread operator in JavaScript, denoted by three consecutive dots (...), is a powerful feature introduced in ES6 that allows for the expansion of iterable objects (like arrays, strings, or objects) into individual elements or properties. It essentially "spreads out" the contents of an iterable into a new context where multiple elements or properties are expected.  */

const arrOne = ['Jan', 'Feb', 'Mar', 'Apr', 'May'];
let arrTwo;
(function() {
    arrTwo = [...arrOne];
    arrOne[0] = 'potato';
}) ();
console.log(arrOne);
console.log(arrTwo);


// 71] Use destructuring assignment to assign various from objects

/* Destructuring assignment in JavaScript is a feature introduced in ECMAScript 2015 (ES6) that provides a concise and convenient way to extract values from arrays or properties from objects and assign them to distinct variables. It allows for more readable and efficient code when working with structured data.  */

// example - 1
var voxel = {x : 3.6, y : 7.4, z : 6.54};

var x = voxel.x;
var y = voxel.y;
var z = voxel.z;

const {x : aa, y : bb, z : cc} = voxel;
console.log(voxel);

// example - 2
const AVG_TEMPERATURES = {
    today : 75.9,
    tomorrow : 79
};
function getTempOfTomorrow(avgTemperatures) {
    const {tomorrow : getTempOfTomorrow} = avgTemperatures;
    return getTempOfTomorrow;
};
console.log(getTempOfTomorrow(AVG_TEMPERATURES));


// 72] Destructuring Assignment with nested objects
const FORCAST = {
    today : {min: 72, max: 83},
    tomorrow : {min : 73.3, max : 84.6}
};

function getMaxOfTomorrow(forcast) {
    "use strict";
    const {tomorrow : {max : getMaxOfTomorrow}} = forcast;
    return getMaxOfTomorrow;
};

console.log(getMaxOfTomorrow(FORCAST));


// 73] Use destructing assignment to assign variables from arrays

// part - 1
const [xx, yy, , zz] = [1, 2, 3, 4, 5, 6];
console.log(xx, yy, zz);

// part - 2 (swapping of two numbers)
let a1 = 3; let b1 = 6;
let arr = [];

arr.push(a1, b1);
console.log(arr);

let array = [];
(() => {
    "use strict";
    [a1, b1] = [b1, a1];
    array.push(a1, b1);
}) ();
console.log(array);


// 74] Use destructuring operator with the rest operator
const source = [1, 2, 3, 4, 5, 6, 7];
function removeTheFirstTwo(list) {
    const [, , ...arrays] = list;
    return arrays;
};
const arrays = removeTheFirstTwo(source);
console.log(source);
console.log(arrays);


// 75] use destructing assignment to pass an object as a function's parameter
const stats = {
    max : 56.78,
    standard_deviation : 4.38,
    median : 34.54,
    mode : 23.87,
    min : -0.78,
    average : 35.85
};

const half = (function () {
    return function half({ max, min }) {
        return (max + min) / 2.0;
    };
}) ();
console.log(stats);
console.log(half(stats));


// 76] create strings using template literals

/* Template literals, also known as template strings, are a feature introduced in ECMAScript 2015 (ES6) that provide a more flexible and powerful way to create strings in JavaScript. They offer several advantages over traditional string concatenation using the + operator or escaping characters. */

// example
const person = {
    name : "Zodiac Hasbro",
    age : 56
};
const greeting = `Hello , my name is ${person.name}
                  I am ${person.age} years old.`;
console.log(greeting);

// coding challenge
const result = {
    success : ["max-length", "no-amd", "prefer-arrow-function"],
    failure : ["no-var", "var-on-top", "linebreak"],
    skipped : ["id-blacklist", "no-due-keys"]
};

function makeList(arr) {
    const resultDisplayArray = [];
    for (let i = 0; i < arr.length; i++){
        resultDisplayArray.push(`<li class="text-warning">${arr[i]}</li`);
    }
    return resultDisplayArray;
};
const resultDisplayArray = makeList(result.success);
console.log(resultDisplayArray);


// 77] Write concise object literals declarations using simple fields
const createPerson = (names, age, gender) => ( {names, age, gender} );
console.log(createPerson("Josh", 20, "male"));

// traditional method
const createPersons = (namez, agez, genderz) => {
    return {
        namez: namez,
        agez: agez,
        genderz: genderz
    }
};
console.log(createPersons("Josh", 20, "male"));

// 78] write concise declarative function
const bicycle = {
    gear : 2,
    setGear(newGear) {
        "use strict";
        this.gear = newGear;
    }
};
bicycle.setGear(3);
console.log(bicycle.gear);


// 79] use class syntax to define a constructor function

/* In JavaScript, a constructor function is a regular function used to create and initialize objects. It acts as a blueprint or template for creating multiple instances of objects with similar properties and methods.  */

class spaceShuttle {
    constructor(targetPlant){
        this.targetPlant = targetPlant;
    }
};
var zeus = new spaceShuttle("Jupiter");
console.log(zeus.targetPlant);

// example
function makeClass() {
    class vegetables {
        constructor(vegan) {
            this.vegan = vegan;
        }
    }
    return vegetables;
};
const vegetables = makeClass();
const carrot = new vegetables("carrot");
console.log(carrot.vegan);


// 80] Use getters and setters to control access to an object

/* In JavaScript, getters and setters are special methods within an object or class that allow you to control how properties are accessed and modified. They provide a way to encapsulate data and add logic to property interactions, similar to how methods are used in other object-oriented programming languages. */

function makeClasses() {
    class thermostat {
        constructor(temp) {
            this._temp = 5/9 * (temp - 32);
        }
        get temperature(){
            return this._temp;
        }
        set temperature(updatedTemp) {
            this._temp =  updatedTemp;
        }
    }
    return thermostat
};
const thermostat = makeClasses();
const thermos = new thermostat(76);
let temp = thermos.temperature;
thermos.temperature = 26;
temp = thermos.temperature;
console.log(temp);


// 81] Understand the differences between import and require

/* The core difference between require and import in JavaScript lies in the module system they belong to:
require: This is part of the CommonJS module system, primarily used in Node.js environments.
import: This is part of the ECMAScript Modules (ESM) standard, which is the native module system for modern JavaScript in both browsers and recent Node.js versions. */

/* import and export are keywords used to manage modules, which are self-contained units of code designed for reusability and organization. They allow you to share code between different JavaScript files, promoting modularity and maintainability in larger applications. */

/* In JavaScript, toUpperCase() and toLowerCase() are built-in string methods used to change the case of characters within a string. */


// the example for this topic is shown in index.js and string_function.js
/* To eliminate the (node:17984) warning and ensure Node.js correctly interprets your modules from the start, you need to explicitly declare that your project is using ES Modules. You can do this by adding "type": "module" to your package.json file. and for that we need to create the package.json file. */


// 82] Slice method

/* In JavaScript, slice() is a method that returns a shallow copy of a portion of an array or a string into a new array or string object, respectively. It does not modify the original array or string.  */

const originalArray = [1, 2, 3, 4, 5];
const newArray = originalArray.slice(1, 4); // Extracts elements from index 1 up to (but not including) index 4
console.log(newArray); // Output: [2, 3, 4]
console.log(originalArray); // Output: [1, 2, 3, 4, 5] (original array remains unchanged)


/* 83] User input function */
// html user input function example is in .js/index.html

// user input function in javascript file 
import { createInterface } from 'readline';
const r1 = createInterface({
    input: process.stdin,
    output: process.stdout
});
r1.question("What is your favorite color ? ", (answer) => {
    console.log(`you said you favorite color is ${answer}`);
    r1.close();
});