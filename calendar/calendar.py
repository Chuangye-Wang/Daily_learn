# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:35:57 2021

@author: ustcw
"""
import sys

class Calendar:
    """
    Given the month, day, and year, return which day of the week it falls on according to the Gregorian calendar.
    For month, use 1 for January, 2 for February, and so forth. Returns 0, 1, 2, ... for Monday, Tuesday, Wednesday, ....
    """
    def day(self, month, day, year):
        y = year - int((14 - month) / 12)
        x = y + int(y/4) - int(y/100) + int(y/400)
        m = month + 12 * int(((14 - month) / 12)) - 2
        d = (day + x + int((31*m)/12)) % 7
#        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
#        d = (day + x + t[month-1]) % 7
        
        return d

    # return true if the given year is a leap year
    def isLeapYear(self, year):
        if((year % 4 == 0) and (year % 100 != 0)): return True
        if(year % 400 == 0): return True
        return False

def showCalendar(month, year):
    calendar = Calendar();
    # months[i] = name of month i
    months = [
        "",                               # leave empty so that months[1] = "January"
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]

    # days[i] = number of days in month i
    days = [
        0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]

    # check for leap year
    if (month == 2 and calendar.isLeapYear(year)): days[month] = 29


    # print calendar header
    print("", months[month], " ", year);
    print(" S  M Tu  W Th  F  S");

    # starting day
    d = calendar.day(month, 1, year)

    # print the calendar
    for i in range(0, d):
        print("   ", end = "")
    for i in range(1, days[month]+1) :
        print("%2d " % i, end = "");
        if (((i + d) % 7 == 0) or (i == days[month])): print()
        
    return 1

if __name__ == "__main__":
    """ for command line arguments input """
    month = int(sys.argv[1]);    # month (Jan = 1, Dec = 12)
    year = int(sys.argv[2]);     # year
    showCalendar(month, year);
    """ for funciton calling """
    
#    month = 7
#    year = 2005
#    showCalendar(month, year)