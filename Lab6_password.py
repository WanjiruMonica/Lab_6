# A program that asks for a password till user gets it right.


def password():
    pass_word = input("Enter the password: ") # if the password is only integeres, use int(input)
    correct_password = 'monica1234'  # The single quote is to make it a string.
    
    while pass_word != correct_password :
        print("Please try again")
        pass_word = input("Enter the password: ")
    print("WELCOME:)") # Prints once the user gets it right.
     


password()
        
