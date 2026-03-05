// Arrow functions
// This is a function that was ntroduced in the ECMAScript 6 and they give us the latest/modern way of defining functions in a compact manner.
// At times the arrow functions can be said to be anonymous functions. this is because they usethe names of the variables they are contained in.
// The syntax of the arrow functions is as follows:

const sayHello = () => {
    console.log("Hello, welcome to JavaScript!")
}
sayHello();

// If the function has only one statement, we can omit the curly braces and the return keyword if it's a single expression. For example:
const add = (a, b) => a + b;
console.log("The sum of 5 and 3 is:", add(5, 3));

// If the function has only one parameter, we can omit the parentheses around the parameter. For example:
const square = x => x * x;
console.log("The square of 4 is:", square(4));

// create an arrow function that is able to find the productof three numbers
const product = () => {
    a = 5
    b = 10
    c = 15
    console.log("The product of the three numbers is:", a * b * c)
}
product();