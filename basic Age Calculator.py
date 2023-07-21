txt = '"""AGE CALCULATOR"""'
x = txt.center(50)
print(x)

import datetime
date = datetime.datetime.now()

flag = True
while(flag):
  
  print("\nEnter your date of birth:\n")
  year = int(input("Enter a year :"))
  month = int(input("Enter a month :"))
  day = int(input("Enter a day :"))
  print("\nYour birth date is :", year, '/', month, '/', day,)
  da = datetime.datetime(year, month, day)

  age = date - da
  ans=(age / 365).days
  print("Your age is:",ans,"year" )

  input_flag = input("\nPress y to continue :\n")
  if (input_flag == 'y'):
   flag = True
  else:
   flag = False
  print("-----------------------------------------")