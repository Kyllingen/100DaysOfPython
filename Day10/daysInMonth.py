def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if year < 1 or month < 1 or month > 12:
        return "Invalid input"
    
    numDays = monthDays[month - 1]
    if month == 2 and isLeap(year):
        numDays += 1
        
    return numDays

#input
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = daysInMonth(year, month)
print(days)