import UIKit

// Step 1: Create a class to represent a local file with two stored properties
class LocalFile {
    let name: String
    let fileExtension: String
    
    // Step 2: Declare an init method to prepare class for initialization later
    init(name: String, fileExtension: String) {
        self.name = name
        self.fileExtension = fileExtension
    }
    
    // Step 3: Create a computed property that returns a full file name
    var fullFileName: String {
        return name + "." + fileExtension
    }
}

// Step 4: Create a class instance to verify that it works as expected
let file = LocalFile(name: "image", fileExtension: "png")
print(file.fullFileName)

class Product   {
  var price: Int = 5
}
var product1 = Product()
var product2 = product1
product1.price = 20
print("\(product1.price), \(product2.price)")
