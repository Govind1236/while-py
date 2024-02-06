import random
number = random.randint(1, 50)
print("--------Welcome---to---Guess Game--------")
print("Guess the number between 1 to 50")
guess_num = False
while not guess_num:
    guess = int(input("Enter a number: "))
    if(guess < number):
        print("Too low Try again")
    elif(guess > number):
        print("Too high Try Again")
    else:
        print("congratulation you made the correct guess", number)
        guess_num = True