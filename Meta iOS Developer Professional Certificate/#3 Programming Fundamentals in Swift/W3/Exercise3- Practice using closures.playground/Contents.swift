import UIKit

var goldBars = 0
let unlockTreasureChest = { (inventory: inout Int) in
    inventory += 100
}
unlockTreasureChest(&goldBars)
print(goldBars) // Output: 100


