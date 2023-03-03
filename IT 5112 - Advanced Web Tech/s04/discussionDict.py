# Dictionaries are used to store data values in key:value pairs
# Created within curly braces where the key value pairs are denoted with (key : value)

# player1 = {
#     "name" : "Dragic",
#     "age" : 18,
#     "position" : "Point Guard",
#     "isSigned" : False,
#     "skills" : ["Passing", "Shooting", "Spacing"]
# }

# print(player1)

# # Getting the number of key-value pairs using "len()"
# print("The number of key-value pairs:", len(player1))

# # Accessing values in the dictionary
# print(player1["position"])

# # Getting list of all keys in the dictionary with "keys()"
# print(player1.keys())

# # Getting list of all values in the dictionary with "values()"
# print(player1.values())

# # Getting list of all items in the dictionary with "items()"
# print(player1.items())

# Adding key-value pairs through assigning with an index key or using the "update()" method
# player1["nationality"] = "Slovenian"
# player1.update({"lastTeam" : "Chicago Bulls"})
# print(player1)

# # Deleting entries with "pop()" or "del"
# player1.pop("nationality")
# del player1["lastTeam"]
# print(player1)

# # "clear()" method for emptying the dictionary
# player2 = {
#     "name" : "Adebayo",
#     "age" : 25
# }
# print(player2)
# player2.clear()
# print(player2)

# # Looping through dictionaries with for loops
# for key in player1:
#     print(f"The value of {key} is {player1[key]}")

# # Nesting dictionaries
# player3 = {
#     "name" : "Butler",
#     "age" : 32,
#     "position" : "Forward",
#     "isSigned" : True,
#     "skills" : ["Shooting", "Cutting", "Defense", "Playmaking"]
# }

# classRoom = {
#     "nbaPlayer1": player1,
#     "nbaPlayer2": player3
# }

# print(classRoom)

# # Mini-Exercise
# 1. Create a car dicitonary with the following keys: brand, model, year of make, color
# 2. Print the following statement from the details: "I own a <color> <brand> <model> and it was made in <year of make>."

car1 = {
    "brand" : "BMW",
    "model" : "Unicycle",
    "yearOfMake" : 2017,
    "color" : "crimson red"
}

car2 = {
    "brand" : "Toyota",
    "model" : "Floating Chair V5",
    "yearOfMake" : 2024,
    "color" : "moldy green"
}

car3 = {
    "brand" : "Ford",
    "model" : "Horse and Carriage",
    "yearOfMake" : 1733,
    "color" : "brown"
}

carShow = {
    "displayCar1" : car1,
    "displayCar2" : car2,
    "displayCar3" : car3
}

for i in carShow:
    print(f"I own a", carShow[i]['color'], carShow[i]['brand'], carShow[i]['model'], "and it was made in", carShow[i]['yearOfMake']) 

