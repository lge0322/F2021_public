// Variable to store how many seconds since the page has loaded
var secs = 0;

// Variables to store the location of the most recent mouse press
var x = -1;
var y = -1;

// Uses builtin utilities (similar to Python's) to randomly generate an (r, g, b) color
function randomColor() {
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);
    return `rgb(${r},${g},${b})` // Basically an f-string
}

// Changes the color of the text in paragraphA to a random color
function changeSectionColor() {
    var color = randomColor();
    document.getElementById("paragraphA").style.color = color;
}

// Takes in the id of an HTML element and changes the color of all text in that
// element to a random color
function mousePressed(event) {
    document.getElementById("paragraphA").innerHTML = `Clicking Button 1 will randomize the color of this text. This is done by giving Button 1 an onclick property which calls a function when the mouse cicks on the button. Clicking anywhere will also change the text. This is done by binding window.onclick to a function. Most recent mouse press: (${event.x}, ${event.y})`;
}

// Takes in a keyboard event and appends that key to paragraphB
function keyPressed(event) {
    document.getElementById("paragraphB").innerHTML += event.key;
}

// Called when the mouse hovers over Button 2
function disco() {
    document.getElementById("paragraphC").innerHTML = "Moving the mouse away from Button 2 will change the text back. This is done by giving Button 2 an onmouseout property which calls another function when the mouse stops hovering over the button.";
}

// Called when the mouse moves away from Button 2
function party() {
    document.getElementById("paragraphC").innerHTML = "Hovering over Button 2 cuases this text to change. This is done by giving Button 2 an onmouseover property which calls a function when the mouse begins to hover over the button.";
}

// Displays the dimensions of the page in paragraph D
function windowResized() {
    document.getElementById("paragraphD").innerHTML = `Resizing the web page will cause this text to change. This is done by binding the event window.onresize to a function. Width: ${window.innerWidth}px\nHeight: ${window.innerHeight}px`;
}

function timerFired() {
    secs += 1;
    document.getElementById("paragraphE").innerHTML = "Every 1 second, the number at the end of this paragraph goes up by one. This is done by creating a function and telling JS to call this function infinitely with a certain time interval. Time since page was opened: " + secs;
}

// Displays the location of the mouse in paragraph F
function mouseMoved(event) {
    document.getElementById("paragraphF").innerHTML = `Every time the mouse is moved, this text changes. This is done by binding the event window.mousemove to a function. Location of the mouse: (${event.x}, ${event.y})`;
}

// When the mouse is pressed, mousePressed will automatically be called
window.onmousedown = mousePressed;

// When an alphabetic, numeric, or punctuation key is pressed, keyPressed will
// automatically be called
window.onkeypress = keyPressed;

// When the window is resized, windowResized is automatically called
window.onresize = windowResized;

// When the mouse is moved, mouseMoved is automatically called
window.onmousemove = mouseMoved;

// JavaScript will now call timerFired every 1000 milliseconds 
window.setInterval(timerFired, 1000);