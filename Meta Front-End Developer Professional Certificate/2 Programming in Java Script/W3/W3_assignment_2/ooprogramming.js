// Task 1: Code a Person class
class Person {
    constructor(name = "Tom", age =20, energy =100) {
        this.name = name;
        this.age = age;
        this.energy = energy;
    }
    sleep() {
        this.energy += 10;  
    }
    doSomethingFun(){
        this.energy -= 10;
    }
}
// Task 2: Code a Worker class
class Worker extends Person {
    constructor(name, age, energy, xp = 20, houryWage = 10){
        super( name, age, energy);
        this.xp = xp;
        this.houryWage = houryWage;
    }
    goToWork(){
        xp += 10;
    }
}
// Task 3: Code an intern object, run methods
function intern(){ 
    let intern = new Worker(name = "Bob", age = 21, energy =110, xp =0, houryWage = 10);
    intern.goToWork();
    return intern;
}

// Task 4: Code a manager object, methods
function manager() {
    let manager = new Worker(name = "Alice", age = 30, energy = 120, xp = 100, houryWage = 30);
    manager.doSomethingFun();
    return manager;

}

class Animal {
    constructor(lg) {
        this.legs = lg;
    }
}

class Dog extends Animal {
    constructor() {
        super(4);
    }
}

var result = new Dog();
console.log(result.legs);

class Person {
    sayHello() {
        console.log("Hello");
    }
}

class Friend extends Person {
    sayHello() {
        console.log("Hey");
    }
}

var result = new Friend();
result.sayHello();