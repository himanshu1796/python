#!/bin/python3

from random import randint #to generate random number
player = input('rock (r), paper(p) or scissors (s)?') #input from player
print(player, 'vs',end=' ')

chosen = randint(1,3) #Random number is given to the variable chosen
#print(chosen)

# Initials of rock, paper and scissors are given to the number that will be generated randomly
if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 's'
else :
    computer = 'p'
print (computer)

# if-else block to define the wining conditon
if computer == player:
    print('draw')
elif player == 'r' and computer == 'p':
    print ('Computer wins!')
elif player == 'r' and computer == 's':
    print (' Player wins!')
elif player == 's' and computer == 'p':
    print ('Player wins!')
elif player == 's' and computer == 'r':
    print ('Computer wins!')
elif player == 'p' and computer == 's':
    print ('Computer wins!')
elif player == 'p' and computer == 'r':
    print ('Player wins!')
    