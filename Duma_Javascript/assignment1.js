// Assignment 1

let distance = 645
if (distance >= 0 && distance <= 100) {
    console.log("Pay 5 USD") // Output: Pay 5 USD

} else if (distance > 100 && distance <= 500) {
    console.log("Pay 10 USD") // Output: Pay 10 USD

} else if (distance > 500 && distance <= 1000) {
    console.log("Pay 20 USD") // Output: Pay 20 USD

} else if (distance > 1000) {
    console.log("Pay 40 USD") // Output: Pay 40 USD

} else {
    console.log("Invalid distance") // Output: Invalid distance
}