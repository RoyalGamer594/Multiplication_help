'''This is 'Multiplication Help'.'''





# 1.Enter full screen.
# 2.Click the button 'Run' on the top (these instructions are only for a Mac device).




















































print('Multiplication Help')
print('-'*30)
print("Introduction- This app helps you learn the multiplication. Like try the number 957345273456 or something like that. After you select the number simply click 'Enter'.")
print('-'*30)
print()
while True:
  try:
    number = int(input("Enter a Number of Your Choice:\n"))
  except:
    print("Sorry! You have not entered a Number")
  else:
    for x in range(12):
      print(f'{number} x {x+1} = {number * (x+1)}')
    
print()
print("Thank You for using this app")
print()
print()
print("*Made by Pranav") 


