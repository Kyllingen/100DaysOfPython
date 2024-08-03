#Functions with outputs

def formatName(firstName, lastName):
    return f"{firstName} {lastName}"

fullName = formatName("John", "Doe")
print(fullName) 

def formatTitleCase(firstName, lastName):
    return f"{firstName.title()} {lastName.title()}"
titleName = formatTitleCase("john", "doe")
print(titleName)