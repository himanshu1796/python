import random #to use random charachters
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,!@#$%^&*()_<>|\?.' # super set for subsets of passwords
length = int(input('Enter the password length '))
password = ' '

value = input('you want to create single password of multiple password?')
#if block to choose sinfle passowrd or multiple passwords
if value == 'single' or value== 'SINGLE':
#For creating a single random password
   for c in range(length):
     password += random.choice(chars)
   print ('Your password is')
   print(password)
elif value=='multiple' or 'MULTIPLE':
#For creating multiple random passwords
     number = int(input('enter the number of password u want'))
     for p in range(number):
        password = ' '
        for c in range(length):
          password += random.choice(chars)
        print(password)