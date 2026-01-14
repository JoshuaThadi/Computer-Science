const fs = require("fs").promises;

function handleSynchronousError() {
  try {
    let result = 10 / 0;
    console.log("Synchronous result: " + result);
  } catch (error) {
    console.log("Synchronous error: " + error.message);
  }
}

async function handleAsynchronousError() {
  try {
    const data = await fs.readFile("non-existent-file.txt", "utf-8");
    console.log("File Content: " + data);
  } catch (error) {
    console.log("Asynchronous error: " + error.message);
  }
}

function handlePromiseError() {
  fs.readFile("non-existent-file.txt", "utf-8")
    .then((data) => {
      console.log("File Content: " + data);
    })
    .catch((error) => {
      console.log("Error caught in Promise: " + error.message);
    });
}

async function main() {
  console.log("=== Synchronous Exception Handling ===");
  handleSynchronousError();
  
  console.log("=== Asynchronous Exception Handling ===");
  await handleAsynchronousError();
  
  console.log("=== Promise Exception Handling ===");
  handlePromiseError();
}

main();
