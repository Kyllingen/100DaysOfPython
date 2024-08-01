country = input("Which country did you visit?\n") #Add country of name
visits = int(input("How many times have you visited?\n")) #Number of visits
listOfCities = eval(input("Which cities have you visited?\n")) #create list from formatted string

travelLog = [
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

def addNewCountry(country, visits, listOfCities):
    travelLog.append({
        "country": country,
        "visits": visits,
        "cities": listOfCities
    })

addNewCountry(country, visits, listOfCities)
print(f"I've been to {travelLog[2]['country']} {travelLog[2]['visits']} times.")
print(f"My favourite city was {travelLog[2]['cities'][0]}.")