# Ever wanted to generate a calendar very fast
# This code allows you to do exactly that
# Email : peterwahomemaina003@gmail.com | Whatsapp : +254794797796

from calendar import TextCalendar
year = int(input("Enter the year : "))
cal = TextCalendar(firstweekday=6)
print(cal.formatyear(year, 2, 1, 8, 3))