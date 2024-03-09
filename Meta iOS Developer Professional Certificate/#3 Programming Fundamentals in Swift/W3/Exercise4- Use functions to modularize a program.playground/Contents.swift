import UIKit

var goldBars = 100
func spendTenGoldBars(from inventory: inout Int, completion: (Int) -> Void) {
    inventory -= 10
    completion(inventory)
}
print("You had \(goldBars) gold bars.")

spendTenGoldBars(from: &goldBars) { (remainingGoldBars) in
    print("You spent ten gold bars.")
    print("You have \(remainingGoldBars) gold bars.")
}

