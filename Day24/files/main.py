#Read files

file = open("my_text.txt")

contents = file.read()
print(contents)

file.close() #free resources


# open and close through "with". dont need to close
with open("my_text.txt") as file:
    contents = file.read()
    print(contents)
    
#write to file (overwrite)
with open("my_text.txt", "w") as file:
    file.write("Some new text")
    
#append to file
with open("my_text.txt", "a") as file:
    file.write("\nappended text")
    
