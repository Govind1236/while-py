import random
number = random.randint(1, 50)
print("--------Welcome---to---Guess Game--------")
print("Guess the number between 1 to 50")
guess_num = False
attempts = 0
while not guess_num:
    guess = int(input("Enter a number: "))
    attempts = attempts + 1
    if(guess < number):
        print("Too low Try again")
    elif(guess > number):
        print("Too high Try Again")
    else:
        print("congratulation you made the correct guess", number)
        print(f"You made it in" , attempts, "attempt")
        guess_num = True