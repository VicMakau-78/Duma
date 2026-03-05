// String data type
// A string is a series/sequence of characters that are enclosed inside of quotation marks

let name = "Victor Makau" // This is a string variable that contains the name "Victor Makau"
console.log("My name is: ", name) // Output: My name is: Victor Makau
console.log("typeof name is: ", typeof name) // Output: string


// floating point: This is a number that has a decimal point. It is used to represent real numbers that can have fractional parts.

let price = 19.99 // This is a floating point variable that contains the price of an item
console.log("The price of the item is: ", price) // Output: The price of the item is: 19.99
console.log("typeof price is: ", typeof price) // Output: number

// Boolean: This is a data type that can only have two values: true or false. It is used to represent logical values and is often used in conditional statements.

let isAdult = true // This is a boolean variable that indicates whether a person is an adult or not
let isRegistered = false // This is a boolean variable that indicates whether a user is registered or not
console.log("Is the person an adult? ", isAdult) // Output: Is the person an adult? true
console.log("Is the user registered? ", isRegistered) // Output: Is the user registered? false
console.log("typeof isAdult is: ", typeof isAdult) // Output: boolean
console.log("typeof isRegistered is: ", typeof isRegistered) // Output: boolean

// Undefined is a data type that has been declared but there is no value assigned to it.
let country; // This variable is declared but not assigned a value, so it is undefined
console.log("The value of country is: ", country) // Output: The value of country is: undefined

// null data type: it is a data type that contains null values

let username = null // This variable is assigned a null value, indicating that it has no value
console.log("The value of username is: ", username) // Output: The value of username is: null

// Assignemnt: research and come up with examples of the following data types:

// Object data type is a collection of key value pairs where each key (also called a property) is associated with a value. It is a fundamental building block in JavaScript and can be used to represent real-world objects, such as people, cars, or products.

let person = {
    name: "Victor",
    age: 25,
    isStudent: false
}
console.log("The person object is: ", person.name) // Output: The person object is: Victor
console.log("typeof person is: ", typeof person) // Output: typeof person is: object


// Array data type is a data type that is used to store multiple values in a single variable. It is an ordered collection of values, where each value is identified by an index.

let fruits = ["apple", "banana", "orange", "grape"] // This is an array that contains a list of fruits
console.log("The fruits array is: ", fruits)
console.log("typeof fruits is: ", typeof fruits)