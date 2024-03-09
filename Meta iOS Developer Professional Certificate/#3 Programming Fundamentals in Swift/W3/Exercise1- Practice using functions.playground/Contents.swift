import UIKit

// Step 1: Declare a variable called goldBars and set its value to 0
var goldBars = 0

// Step 2: Define a function called unlockTreasureChest with return type Int and parameter inventory of type Int
func unlockTreasureChest(inventory: Int) -> Int {
    // Step 5: Update the body - return inventory plus 100
    return inventory + 100
}
// Step 7: Call the function three times to simulate finding three treasure chests
goldBars = unlockTreasureChest(inventory: goldBars)
print(goldBars) // Output: 100

goldBars = unlockTreasureChest(inventory: goldBars)
print(goldBars) // Output: 200

goldBars = unlockTreasureChest(inventory: goldBars)
print(goldBars) // Output: 300

