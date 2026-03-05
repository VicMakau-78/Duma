// Task 1
// write a for loop and a while loop to find the largest number in the array: (10,20,4,45,99,1)
let numbers = [10, 20, 4, 45, 99, 1];
let max = numbers[0];

// For loop
for (let x = 1; x < numbers.length; x++) {
    if (numbers[x] > max) {
        max = numbers[x];
    }
}
console.log("Max using for loop:", max);

// While loop
let y = 1;
max = numbers[0];
while (y < numbers.length) {
    if (numbers[y] > max) {
        max = numbers[y];
    }
    y++;
}
console.log("Max using while loop:", max);

// Task 2
// Write `a for loop and while loop to print the multiplication table of 5 from 5*1 to 5*10
// For loop
console.log("Multiplication table of 5 using for loop:");
for (let i = 1; i <= 10; i++) {
    console.log("5 * " + i + " = " + (5 * i));
}

// While loop
let j = 1;
console.log("Multiplication table of 5 using while loop:");
while (j <= 10) {
    console.log("5 * " + j + " = " + (5 * j));
    j++;
}


// Task 3
// Functions
// Students to create a function named mycountry(), the function to print /log 5 messages explaining about my country. call tis function.
function myCountry() {
    console.log("My country is Kenya.");
    console.log("Kenya is located in East Africa.");
    console.log("The capital city of Kenya is Nairobi.");
    console.log("Kenya is known for its wildlife and national parks.");
    console.log("The Country's President is Dr. William Ruto.");
}
myCountry();
