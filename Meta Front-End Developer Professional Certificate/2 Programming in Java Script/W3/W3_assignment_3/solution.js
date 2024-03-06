// Task 1
const dairy = ['cheese', 'sour cream', 'milk', 'yogurt', 'ice cream', 'milkshake'];

function logDairy() {
    for(let item of dairy) {
        console.log(item);
    }
}

// call the function to see the output on the console
logDairy();

// Task 2
const animal = {
    canJump: true
};
const bird = Object.create(animal);
bird.canFly = true;
bird.hasFeathers = true;

function birdCan() {
    for(let [key, value] of Object.entries(bird)) {
        console.log(`${key}: ${value}`);
    }
}

// call the function to see the output on the console
birdCan();


// Task 3
function animalCan() {
    for (let property in bird) {
        console.log(`${property}: ${bird[property]}`);
    }
}

// call the function on 'bird' object:
animalCan();