progammingDictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieve an item using key
print(progammingDictionary["Bug"])

#add another item to the dictionary
progammingDictionary["Loop"] = "The action of doing something over and over again."

#edit an item in the dictionary
progammingDictionary["Bug"] = "An error in a program that prevents the program from running as expected. It is a feature, not a bug."

print(progammingDictionary["Bug"])

#loop through the dictionary. It just returns keys, so need to access the element
for key in progammingDictionary:
    print(key + ": " + progammingDictionary[key])