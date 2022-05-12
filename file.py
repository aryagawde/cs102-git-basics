# given a year as input, find out the next leap year:

def leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            return (year % 400 == 0)
        else:
            return True
    else:
        return False

def next_leap_year(year: int) -> int:
    remainder = 4 - (year % 4)
    next_year = year + remainder
    if leap_year(next_year):
        return next_year
    else:
        return next_leap_year(next_year)
