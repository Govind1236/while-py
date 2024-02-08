def User_input(fname , lname):
    if fname == 'user' and lname == 'trak':
        result_ = "Correct"
    else:
        result_ = "Incorrect"
    return result_
fname = input('Enter First Name: ')
lname = input('Enter Last Name: ')
result_ = User_input(fname, lname)
print("The User has enter",result_, "input")