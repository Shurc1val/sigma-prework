from datetime import date

def ask_user_for_date(msg):
  #Keeps requesting an input from the user with the given msg until an integer is entered
  while True:
    periods = input(msg).split("-")
    if len(periods) == 3 and all([True for period in periods if period.isnumeric()]):
        day = int(periods[0])
        month = int(periods[1])
        year = int(periods[2])
        if valid_date(day,month,year):
            break
    print("Invalid input - please try again.\n")
  return day,month,year

def valid_date(day,month,year):
   #Checks whether the date given is valid
   days_in_month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
   if year < 0 or year > 9999:
      return False
   if month < 0 or month > 12:
      return False
   if day < 0 or day > days_in_month[month]:
     return False
   return True

def years_passed(date_1,date_2):
   dates = dates_ascending(date_1,date_2)
   date_1 = dates[0]
   date_2 = dates[1]
   #Wanted to make this much simpler by using * to unpack list, but kept getting errors

   years = date_2[2] - date_1[2]
   if date_2[1] < date_1[1]:
      years -= 1
   elif date_2[1] == date_1[1]:
      if date_2[0] < date_1[0]:
         years -= 1
   return years
 
def dates_ascending(date_1,date_2):
   #Function to sort dates into ascending order
   return sorted([date_1,date_2], key = lambda date: (date[2],date[1],date[0]))


today = [int(period) for period in str(date.today()).split("-")[::-1]]
date = ask_user_for_date("Please enter a date (dd-mm-yyyy): ")
print(years_passed(date, today))
  