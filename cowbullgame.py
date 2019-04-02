# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:30:01 2019

@author: zeinab
Welcome to the Cow and Bull Game. In this game the code will randomely choose a 4 digit number.
You should guess the number. For every digit that you guessed correctly in the right position you will get a "cow".
For every digit that you guessed correctly but in the wrong possition you will get a "bull". 
For Example, the random number is 1234. 
If you guess 1354 you will get 2 cow (for 1 and 4) and 1 bull (for 3).
The game ends when you guess the number correctly. 
Type "break" if you want to end the game. 
Note: the number could have duplicate digits! 

enjoy!
"""

import random 


def get_digits(number):
    #this function seperate the digits of a number and return a list containing all the digits.
    digits=[]
    while number>0:
        number, digit = divmod(number, 10)
        digits.append(digit)
    return digits
   
    
def compare(digits_guess,digits_num):
    #This function scores the guess.
    #1 cow for every correct digit in th right place.
    #1 bull for every correct digit in wrong position.
    bull=0
    numbers_zipped=list(zip(digits_guess,digits_num)) 
    in_correct_place= [x for (x,y) in numbers_zipped if x==y]
    cow=len(in_correct_place)
    the_rest=[(x,y) for (x,y) in numbers_zipped if not x==y]  #removes the cow pairs from the list to deal with the bulls
    guess_el=[x for (x,y) in the_rest]
    num_el=[y for (x,y) in the_rest]
    guess_el_len=len(guess_el)
    for i in range(guess_el_len):   # in the for loop if a digit from guess number (without the cows) is seen in number, will add a bull
        if guess_el[i] in num_el:
            bull +=1
            num_el.remove(guess_el[i]) #remove the element from number list so it won't check it again
    return cow, bull
    

print("Welcome to Cow and Bull Game!")

number=random.randint(1000,10000)

cow=0
count_guesses=0
bull=0

while cow<4:
    guess=input("Please guess the number: \n")
    if guess=="break":
        break
    guess=int(guess)
    count_guesses +=1 
    digits_num=get_digits(number) 
    digits_guess=get_digits(guess)  
    cow, bull=compare(digits_guess,digits_num)
    print("cow:" + str(cow) + ", bull: "+ str(bull))

print("You guessed {} times".format(count_guesses))

 
