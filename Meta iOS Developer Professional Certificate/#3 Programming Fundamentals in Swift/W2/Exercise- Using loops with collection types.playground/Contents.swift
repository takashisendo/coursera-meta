import UIKit

let levelScores = [10, 20, 30, 40, 50, 60, 70]

for (level, score) in levelScores.enumerated() {
    print("The score of level \(level + 1) is \(score).")
}

var gameScore = 0
for score in levelScores {
    gameScore += score
}
print("The final game score is \(gameScore).")

let weeklyTemperatures = ["Monday": 70, "Tuesday": 75, "Wednesday": 80, "Thursday": 85, "Friday": 90, "Saturday": 95, "Sunday": 100]

for (day, temperature) in weeklyTemperatures {
    print("The temperature on \(day) is \(temperature)°F.")
}
let days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
let temperatures = [70, 75, 80, 85, 90, 95, 100]

for index in 0..<days.count {
    print("The temperature on \(days[index]) is \(temperatures[index])°F.")
}
let emptyDictionary: [String: Int] = [:]
if emptyDictionary.count == 0 {
  print("The dictionary is empty!")
} else {
  print("The dictionary isn’t empty!")
}
let emptyDictionary: [String: Int] = ["": 0]
if emptyDictionary.count == 0 {
 print("The dictionary is empty!")
} else {
 print("The dictionary isn’t empty!")
}
