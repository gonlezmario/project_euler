# 1 Jan 1901 to 31 Dec 2000
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:  # Not a century year
            return True
        elif year % 100 == 0 and year % 400 == 0:  # If its a century year it must be divisible by 400
            return True
        else:
            return False

def number_sundays(): 
    
    first_year = 1901
    last_year = 2000
    sunday_counter = 1
    number_day = 0 # Days shifted after month is complete

    for year in range(first_year,last_year+1):
        number_day += 3  # Jan (31-7*4)
        if number_day % 7 == 0:
            sunday_counter += 1
        if is_leap_year(year):  # Leap Feb
            number_day += 1 #(28-7*4)
            if number_day % 7 == 0:
                sunday_counter += 1
        if not is_leap_year(year):  # Regular Feb
            number_day += 0 #(28-7*4)
            if number_day % 7 == 0:
                sunday_counter += 1
        number_day += 3  # Mar
        if number_day % 7 == 0:
            sunday_counter += 1
        number_day += 2  # Apr (30-7*24)
        if number_day % 7 == 0:
            sunday_counter += 1
        number_day += 3  # May
        if number_day % 7 == 0:
            sunday_counter += 1
        number_day += 2  # Jun
        if number_day % 7 == 0:
            sunday_counter += 1
        number_day += 3  # Jul
        if number_day % 7 == 0:
            sunday_counter += 1
        number_day += 3  # Aug
        if number_day % 7 == 0:
            sunday_counter += 1
        number_day += 2  # Sep
        if number_day % 7 == 0:
            sunday_counter += 1
        number_day += 3  # Oct
        if number_day % 7 == 0:
            sunday_counter += 1
        number_day += 2  # Nov
        if number_day % 7 == 0:
            sunday_counter += 1
        number_day += 3  # Dec
        if number_day % 7 == 0:
            sunday_counter += 1

    return sunday_counter

print(number_sundays())



