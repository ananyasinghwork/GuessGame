import random
import math

lower_bound=int(input("Enter the Lower Bound: "))
upper_bound=int(input("Enter the Upper Bound: "))

x= random.randint("You have only ",round(math.log(upper_bound - lower_bound +1,2)),"to guess the number!")

count=0

while(count<math.log(upper_bound - lower_bound +1,2)):
    count +=1

guess = int(input("Guess a number:"))

if(x==guess):
    print("Congrats, You guessed it right!")

elif(x>guess):
    print("You guessed a number that is smaller!")

elif(x<guess):
    print("You guessed a number that is bigger!")

if count >= math.log(upper_bound - lower_bound +1,2):
    print("The correct number is: %d",x)
    print("Better luck next time..")
