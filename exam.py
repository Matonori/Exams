#account
name = input("enter your name: ")
surname = input("enter your surname: ")
number = input("enter your phone number: ")
card = input("enter your credit card credentials: ")

#deposit and withdraw
action = int(input("what would you like to do? press 1 to withdraw, press 2 to deposit, press 3 to exit."))
if action == 1:
    withdraw = int(input("how much would you like to withdraw?"))
    print("thank you, come again!")
if action == 2:
    deposit = int(input("how much would you like to deposit?"))
    print("thank you, come again!")

#exit
if action == 3:
    print("thank you for using the bank program. come again!")