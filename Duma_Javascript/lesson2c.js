// else if statement
let age = 12
if (age < 14) {
    console.log("You are too young to watch this movie.") // Output: You are too young to watch this movie.
} 
else if (age >= 14 && age <= 18) {
    console.log("You are old enough to watch this movie, but you must be supervised.") // Output: You are old enough to watch this movie, but you must be supervised.
} 
else if (age > 18 && age <= 40){
    console.log("You can watch this movie without supervision.") // Output: You can watch this movie without supervision.
} 
else {
    console.log("You are too old to watch this movie.") // Output: You are too old to watch this movie.
}