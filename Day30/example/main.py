
#Exceptions
try:
    file =  open("a_file.txt")
    a_dict =  {"key": "value"}
    print(a_dict['asdf'])
except FileNotFoundError:
    file = open("a_file.txt", "w") 
except KeyError as error_message:
    print(f"The key {error_message} does not exist")  
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File is closed")

#Our own exception
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not e over 3 meters")

bmi = weight / height ** 2
print(bmi)
