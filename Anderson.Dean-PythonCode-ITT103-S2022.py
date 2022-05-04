"""
Author: Dean Anderson
Date Created: 03/05/2022
Course: ITT103 Programming Techniques
Purpose: To calculate and output the commission received by an undefined number of salespersons based 
on certain input and criteria. 
"""
program_terminator = 'yes'
while program_terminator != 'no':


#For each input that the user is required to enter, there is a while loop that contains the 'Value Error' built-in function.
#This ensures that when the user enters an invalid value, the step loops until a valid one is entered.

  while True:
    try:
      salPer_num=int(input("Welcome! Enter saleperson's number - "))
    except ValueError:
      print("Invalid input.")
      continue
    if salPer_num != int: 
      print("Processing... ")

    break

  while True:
    try:
      sal_am=float(input("Enter sales amount - "))
    except ValueError:
      print("Invalid input.")
      continue
    if sal_am != int: 
      print("Processing... ")

      break

  while True:
      try: 
        class_num=int(input("Enter the class number - "))
      except ValueError:
        continue     

      if class_num < 1 or class_num > 3: 
          print("Try again. Re-enter class number")
      else:
          print("Processing...")
          break

  #These if and else statements determines what sales amount and commission rate should be calculated under a particular class.
    
  if class_num == 1:
      if sal_am <= 1000:
          com_rate = 0.06
          cmn= sal_am*com_rate
          
      elif sal_am > 1000 < 2000:
          com_rate = .07
          cmn= sal_am*com_rate

      elif sal_am >= 2000:
          com_rate = 0.1
          cmn= sal_am*com_rate
  else:
    if class_num == 2:
      if sal_am < 1000:
          com_rate = 0.04
          cmn= sal_am*com_rate
      else:
          if sal_am  > 1000:
              com_rate = 0.06
              cmn= sal_am*com_rate

  if class_num == 3:
      com_rate = 0.045
      cmn= sal_am*com_rate

  #This step prints a statement that is displays the overall information when the user completes entering valid inputes.

  print("The total commission of sales person", salPer_num, "is $",cmn, "from a rate of", com_rate, ". Have a nice day")
 
#The program terminator prompts the user whether or not the program should continue. 
  program_terminator=input("To continue, type 'yes'. To exit, type 'no'.")
else:

  while True: # Loop created for input validation.
          message = input("Are you sure you want to exit? Type 'yes' to exit. Or type 'no' to continue. ")
          if message == 'No' or message == 'NO' or message == 'no':
              pass  
              salPer_num=int(input("Welcome! Enter saleperson's number - "))
              sal_am=float(input("Enter sales amount - "))
              class_num=int(input("Enter the class number - "))
              print("The total commission of sales person", salPer_num, "is $",cmn, "from a rate of", com_rate, ". Have a nice day")
              program_terminator=input("To continue, type 'yes'. To exit, type 'no'.")      
               
          elif message == 'Yes' or message == 'YES' or message == 'yes':
              print("Program has ended.")
              break # This breaks out of the outermost loop if exit is entered
          else:
              print("Incorrect input! Try again.\n")
          
