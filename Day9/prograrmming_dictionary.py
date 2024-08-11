progamming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieve an item using key
print(progamming_dictionary["Bug"])

#add another item to the dictionary
progamming_dictionary["Loop"] = "The action of doing something over and over again."

#edit an item in the dictionary
progamming_dictionary["Bug"] = "An error in a program that prevents the program from running as expected. It is a feature, not a bug."

print(progamming_dictionary["Bug"])

#loop through the dictionary. It just returns keys, so need to access the element
for key in progamming_dictionary:
    print(key + ": " + progamming_dictionary[key])