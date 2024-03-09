import UIKit

// Step 1: Declare a variable called goldBars and set its value to 0
var goldBars = 0

// Step 2: Add unsweetened function

// Step 9: Set the in-out parameter value in the body
func incrementInventory(_ inventory: inout Int, by amount: Int = 100) {
    inventory += amount
}

// Step 10: Calling the function
incrementInventory(&goldBars) // Output: 100
print(goldBars)

incrementInventory(&goldBars) // Output: 200
print(goldBars)

incrementInventory(&goldBars) // Output: 300
print(goldBars)

incrementInventory(&goldBars, by: 300) // Output: 600
print(goldBars)

incrementInventory(&goldBars, by: 50) // Output: 650
print(goldBars)

var aClosure = {
  () -> Void in
  print("This is a closure")
}
aClosure()
