// Function with parameters
function greet(name){
    console.log("Hello " + name + "!")
}
// calling the function with arguements
greet("Alice")
greet("Jane")

// Task 1
function myCounty(County){
    console.log("My county is " + County + ".")
}
// calling the function
myCounty("Nairobi")
myCounty("Makueni")
myCounty("Mombasa")
myCounty("Nakuru")
myCounty("Kiambu")

// Task 2 - addition
function addition(num1, num2){
    answer = num1 + num2
    console.log(`The sum of two numbers is: ${answer}`)
}
// calling the function
addition(22, 10)

// Task 3 - subtraction
function subtraction(num1, num2){
    subt = num1 - num2
    console.log(`The difference of the two numbers is: ${subt}`)
}
// calling the function
subtraction(66, 30)

// Task 4 - Multiplication
function multiplication(num1, num2){
    prod = num1 * num2
    console.log(`The Product of the two numbers is: ${prod}`)
}
// calling the function
multiplication(22, 2.2)

//  Task 5 - Simple Interest
function SimpleInterest(p, r, t){
    SI = p * r * t
    console.log(`The Simple Interest of money is: ${SI}`)
}
// Calling the function
SimpleInterest(45000, 0.15, 4)

// Task 6 - Area of a circle
function Circle(pi, r ){
    Ac = pi * r ** 2
    console.log(`The area of a circle is: ${Ac}`)
}
// Calling the function
Circle(3.142, 7)

// Task 7 - Area of a triangle
function Triangle(b, h){
    At = 1/2 * b * h
    console.log(`The area of a triangle is: ${At}`)
}
// Calling the function
Triangle(36, 25)

// Task 8 - BMI
function BMI(w, h){
    Result = w * h / 2
    console.log(`The BMI is: ${Result}`)
}
// Calling the function
BMI(54, 162)