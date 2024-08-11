#Functions with outputs

def formatName(first_name, last_name):
    return f"{first_name} {last_name}"

full_name = formatName("John", "Doe")
print(full_name) 

def formatTitleCase(first_name, last_name):
    return f"{first_name.title()} {last_name.title()}"
title_name = formatTitleCase("john", "doe")
print(title_name)