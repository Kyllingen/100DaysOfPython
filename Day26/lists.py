#old way 
numbers = [1,2,3]
new_list = []

for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
    
print(new_list)

#list comprehension
new_list = [n+1 for n in numbers]
print(new_list)

#letters split
name = "Jonathan"
letters_list = [letter for letter in name]
print(letters_list)

#using range
double_list = [n*2 for n in range(1,5)]
print(double_list)

#list comprehension with if test
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
long_names_upper = [name.upper() for name in names if len(name) > 4]
print(short_names, long_names_upper)
