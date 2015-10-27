def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    

leap_years = [1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008]
not_leap_years = [2001,1971,2003,1973]


print "these are all leap years"
for y in leap_years:
    print y, is_leap_year(y)


print "these are NOT leap years"
for y in not_leap_years:
    print y, is_leap_year(y)
