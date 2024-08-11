def is_leap(year):
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

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if year < 1 or month < 1 or month > 12:
        return "Invalid input"
    
    num_days = month_days[month - 1]
    if month == 2 and is_leap(year):
        num_days += 1
        
    return num_days

#input
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)