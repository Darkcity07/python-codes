txt = '"""calculator"""'
x = txt.center(50)
print(x)


flag = True
while (flag):
  print('press 1st value:', end="")
  a = int(input())
  print('press 2nd value:', end="")
  b = int(input())

  print("press 1 for '+'")
  print("press 2 for '-'")
  print("press 3 for '*'")
  print("press 4 for '%'")

  option = int(input())
  if option == 1:
    print(a, '+', b, '=', a + b)
  elif option == 2:
    print(a, '-', b, '=', a - b)
  elif option == 3:
    print(a, '*', b, '=', a * b)
  elif option == 4:
    print(a, '%', b, '=', a % b)
  else:
    print('wrong operator selected')

  input_flag = input("Press y to continue")
  if (input_flag == 'y'):
    flag = True
  else:
    flag = False

  print("-----------------------------------------")
