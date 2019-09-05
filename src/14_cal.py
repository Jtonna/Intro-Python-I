"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`

  and does the following:

  - If the user doesn't specify any input, your program should
    print the calendar for the current month. The 'datetime'
    module may be helpful for this.
  
  - If the user specifies one argument, assume they passed in a
    month and render the calendar for that month of the current year.
  
  - If the user specifies two arguments, assume they passed in
    both the month and the year. Render the calendar for that
    month and year.
  
  - Otherwise, print a usage statement to the terminal indicating
    the format that your program expects arguments to be given.
    Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# If the user doesnt pass any argument in it just returns the calendar for their current year and month
if len(sys.argv) == 1:
  theMonth = datetime.now().month
  theYear = datetime.now().year
  print('t1' + calendar.month(theYear, theMonth)) 
  quit()

# If the user passes in the month, we shall assume the year they want is the current calendar year
elif len(sys.argv) == 2:
  theMonth = int(sys.argv[1])
  theYear = datetime.now().year
  print('t2' + calendar.month(theYear, theMonth))
  quit()

# If the user passes in a month and year, we give them what they want.
elif len(sys.argv) == 3:
  theMonth = int(sys.argv[1])
  theYear = int(sys.argv[2])
  print('t3' + calendar.month(theYear, theMonth))
  quit()

# If the user passes in more than 3 arguments we give them a usage statement
elif len(sys.argv) > 3:
  print("****USAGE**** \n This program will do one of three things \n 1. If it is ran it will return the current calendar for your month & year \n 2. It will accept you passing in a month in the format of [01] without brackets, and will assume the year you want is the current year \n 3. you can pass in a month in the format of [01] and a year in the format of [1999]. ex [02 1999] but without brackets. It will return the celandar for the respective monthand year. ")
