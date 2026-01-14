/* The Document Object Model (DOM) is a programming interface for web documents. It represents the page so that programs can change the document structure, style, and content. Essentially, the DOM is a tree-like representation of an HTML or XML document that allows programming languages like JavaScript to interact with and modify the elements of a webpage dynamically.  */

// getting and adding elements
const playground = document.getElementById('playground');
playground.append('Wizard');

const magicalOrb = document.createElement('div');
magicalOrb.textContent = 'Magical Orbitary';
playground.appendChild(magicalOrb);


// Modifying text content
/* 
1] innerText: Focuses on visible text: innerText returns the text content of an element as it appears on the screen, respecting the rendered layout, including line breaks and spacing. It's useful when you need to interact with the text that the user actually sees.

2] innerHTML: Focuses on raw HTML: innerHTML returns the HTML markup (including tags, attributes, and text) that exists inside the element. It's useful for manipulating the structure of an element, including adding new elements, modifying existing ones, or retrieving the complete HTML content.

3] textContent: Returns all the text content of the element and its descendants, regardless of whether it's visible on the screen or hidden by CSS.

*/

const scrollOfWisdom = document.createElement('p');
playground.append(scrollOfWisdom);

scrollOfWisdom.innerText = 'Ancient wisdom lies within';
console.log(scrollOfWisdom.innerText);


// Working with HTML content
const spellBook = document.createElement('div');
spellBook.innerHTML = '<p>Spell include: <strong>Levitation</strong> and <em>Invisiblility</em>!</p>';
playground.append(spellBook);


// Removing Elements
/* 
1] removeChild() Method of: Node interface. This means you call it on a parent node to remove one of its children. 
2] remove() Method of: Element interface. This means you call it directly on the element you wish to remove.
*/

const temporaryElement = document.createElement('p');
temporaryElement.textContent = "Now you see me...";
playground.append(temporaryElement);
temporaryElement.remove();

const fruitBasket = document.createElement('div');
fruitBasket.innerHTML = `
    <p>Apple</p>
    <p>Banana</p>
    <p>Coconut</p>
`;
playground.append(fruitBasket);
while (fruitBasket.firstChild) {
    fruitBasket.removeChild(fruitBasket.firstChild);
}


// Working with Attributes
/* 1] The setAttribute() method allows you to set or change the value of an attribute on a specified HTML element.
   2] The getAttribute() method allows you to retrieve the value of a specified attribute from an HTML element. 
*/

const magicWand = document.createElement('div');
magicWand.setAttribute('id', 'wand1');;
magicWand.setAttribute('class', 'magical-item wand');
magicWand.textContent = "Magical wand";
playground.append(magicWand);
console.log(magicWand.getAttribute('class'));
console.log(magicWand.id);
console.log(magicWand.className);

magicWand.id = "wand3";
console.log(playground.append(magicWand.id));


// Working with Data Attributes
/* 
1] dataset: The dataset property, available on any HTML element, acts as an interface to read and write these custom data-* attributes using JavaScript.  
*/

const secretScroll = document.createElement('div');
secretScroll.id = 'secretScroll';
secretScroll.dataset.spellType = 'invisibility';
secretScroll.dataset.components = 'moonlight, shadow essence';
secretScroll.textContent = "Ancient Spell Scroll";

playground.append(secretScroll);
console.log("Spell Type:", secretScroll.dataset.spell);
console.log("Components:", secretScroll.dataset.components.split((',')));


// Manipulating Classes
/*
    1] classList.add(): Function: Adds one or more classes to an element's class list.
    2] classList.remove(): Function: Removes one or more classes from an element's class list.
    3] classList.item(): Function: Returns the class name at a specified index in the element's class list.
    4] classList.replace(): Function: Replaces an existing class with a new class on an element.
*/

const shapeShifter = document.createElement('div');
shapeShifter.textContent = "ShapeShifter";
playground.append(shapeShifter);

shapeShifter.classList.add('magical', 'creature');
console.log("Initial classes:", shapeShifter.className);

shapeShifter.classList.remove('creature');
shapeShifter.classList.add('Humanoid');

console.log("Updated classes:", shapeShifter.className);
shapeShifter.classList.toggle('invisible', Math.random > 0.5);

shapeShifter.classList.replace('Humanoid', 'Beast');
console.log("Third class:", shapeShifter.classList.item(2));


// Inline styles
/* 
    The setInterval() function is commonly used to set a delay for functions that are executed again and again, such as animations. You can cancel the interval using clearInterval() . If you wish to have your function called once after the specified delay, use setTimeout() 
*/

const enchantedGem = document.createElement('div');
enchantedGem.textContent = "Josh";
enchantedGem.style.fontSize = '50px';
enchantedGem.style.transition = 'all 2s';
playground.append(enchantedGem);

setInterval(() => {
    enchantedGem.style.transform = `rotate(${Math.random() * 360}deg)`;
    enchantedGem.style.color = `hsl(${Math.random() * 360}100%, 50%)`;
},2000);

// Event Handling
/* 
    1] addEventListener() -> Purpose: addEventListener() attaches an event handler function to a specified element, which executes when the event occurs.
    2] removeEventListener() -> Purpose: removeEventListener() removes an event listener added with addEventListener(). This is crucial for preventing memory leaks and managing performance.

*/

// example-1
const magicButton = document.createElement('button');
magicButton.textContent = 'Check Spell';
playground.append(magicButton);

magicButton.addEventListener('click', () => {
    alert('Magic sparkles fill the air!');
});

magicButton.addEventListener('mouseover', (event) => {
    event.target.style.backgroundColor = 'purple';
});

magicButton.addEventListener('mouseout', (event) => {
    event.target.style.backgroundColor = '';
});

// example-2
const magicalButton = document.createElement('button');
magicalButton.textContent = 'Check Magic';
playground.append(magicalButton);

function spellCast() {
    alert('Magic spell repeals the air');
}

magicalButton.addEventListener('click', spellCast);
magicalButton.removeEventListener('click', spellCast);


// Creating and removing elements dynamically
const spellList = document.createElement('ul');
playground.append(spellList);

function addSpell(spellName) {
    
    const spell = document.createElement('li');
    spell.textContent = spellName;

    const removeButton = document.createElement('button');
    removeButton.textContent = 'Remove';

    removeButton.addEventListener('click', () => spell.remove());
    spell.append(removeButton);
    spellList.append(spell);

}

addSpell('FireBall');
addSpell('Frost Nova');


// Traversing the DOM
/*
    Traversing the DOM means using JavaScript to navigate this tree structure. It's used to access, manipulate, or locate specific elements or nodes within a webpage. Think of it like moving through a family tree to find specific relatives or information about them. You can move up, down, or sideways within the node hierarchy
*/

/*
    1] firstChild -> Function: Returns the first child node of a specified node.
    2] lastChild -> Function: Returns the last child node of a specified node.
    3] nextSibling -> Function: Returns the next node at the same level (sibling) as the specified node.
    4] PreviousSibling -> Function: Returns the previous node at the same level (sibling) as the specified node.
    5] parentNode -> Function: Returns the parent node of a specified node.
*/

const playGround = document.getElementById('playGround');
const parentElement = document.createElement('div');
const childElement1 = document.createElement('p');
const childElement2 = document.createElement('span');
parentElement.append(childElement1, childElement2);
playGround.append(parentElement);

console.log(parentElement.firstChild);
console.log(parentElement.lastChild);
console.log(childElement1.nextSibling);
console.log(childElement2.previousSibling);
console.log(childElement1.parentNode);


// Creating document fragments
const fragments = document.createElement('li');
for (let i = 0; i < 5; i++) {
    const magicalItem = document.createElement('li');
    magicalItem.textContent = `Magical Item ${i + 1}`;
    fragments.append(magicalItem);
};

const spelList = document.createElement('ul');
playGround.append(spelList);
spelList.append(fragments);


// Using Templates
/*
    The cloneNode() method in JavaScript is a powerful way to create a duplicate of an existing node in the Document Object Model (DOM). You can think of it as taking a blueprint of an element and using it to construct a new, identical element.
*/

const template = document.getElementById('wizard-template');
function createWizard(name, specialty) {
    const wizardElement = template.content.cloneNode(true);
    wizardElement.querySelector('.wizard-name').textContent = name;
    wizardElement.querySelector('.wizard-specialty').textContent = specialty;
    playGround.append(wizardElement);
};

createWizard('Merlin', 'Time Magic');
createWizard('Gandalf', 'Fireworks');



/* 

Accessing Elements:
document.getElementById("id"): Selects a single element by its ID.
document.getElementsByClassName("class"): Returns an HTMLCollection of elements with a specific class.
document.getElementsByTagName("tag"): Returns an HTMLCollection of elements with a specific tag name.
document.querySelector("selector"): Returns the first element matching a CSS selector.
document.querySelectorAll("selector"): Returns a NodeList of all elements matching a CSS selector.

Modifying Elements:
element.textContent = "text": Sets or gets the plain text content of an element.
element.innerHTML = "<b>HTML</b>": Sets or gets the HTML content of an element.
element.style.propertyName = "value": Modifies inline CSS properties (e.g., element.style.color = "red").
element.classList.add("class"): Adds a class to an element.
element.classList.remove("class"): Removes a class from an element.
element.classList.toggle("class"): Toggles a class on an element.
element.setAttribute("attribute", "value"): Sets an attribute's value.
element.removeAttribute("attribute"): Removes an attribute.

Creating & Inserting Elements:
document.createElement("tagName"): Creates a new HTML element.
document.createTextNode("text"): Creates a new text node.
parentElement.appendChild(childElement): Appends a child element to a parent.
parentElement.insertBefore(newElement, referenceElement): Inserts a new element before a reference element.
parentElement.removeChild(childElement): Removes a child element.

Traversing the DOM:
element.parentElement: Returns the parent element.
element.children: Returns an HTMLCollection of all child elements.
element.firstElementChild: Returns the first child element.
element.lastElementChild: Returns the last child element.
element.nextElementSibling: Returns the next sibling element.
element.previousElementSibling: Returns the previous sibling element.

Event Handling:
element.addEventListener("event", handlerFunction): Attaches an event listener.
element.removeEventListener("event", handlerFunction): Removes an event listener.
Form Handling:
form.submit(): Submits a form.
inputElement.value: Gets or sets the value of an input field. 
checkboxOrRadio.checked: Gets or sets the checked state of a checkbox or radio button. 

*/