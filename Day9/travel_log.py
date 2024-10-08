country = input("Which country did you visit?\n") #Add country of name
visits = int(input("How many times have you visited?\n")) #Number of visits
list_of_cities = eval(input("Which cities have you visited?\n")) #create list from formatted string

travel_log = [
    {
        "country": "France", 
        "visits": 12, 
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany", 
        "visits": 5, 
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

def add_new_country(country, visits, list_of_cities):
    travel_log.append({
        "country": country,
        "visits": visits,
        "cities": list_of_cities
    })

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")