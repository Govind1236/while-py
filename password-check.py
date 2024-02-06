pass_word = "Govind@123"
Secret = True
while pass_word:
    password = input("Enter a password: ")
    if password == pass_word:
        print("Correct")
        break
    else:
        print("Enter correct Password")
        
    