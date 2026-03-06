# Dictionary to store users (email: password)
users = { "user1@gmail.com": "pass123",
    "user2@gmail.com": "hello456",
    "user3@gmail.com": "welcome789",
    "user4@gmail.com": "python101",
    "user5@gmail.com": "login2026"}

print("1. New User (Sign Up)")
print("2. Existing User (Login)")

choice = input("Enter your choice (1 or 2): ")

# New User Registration
if choice == "1":
    email = input("enter the email" )
    if email  in users:
        print('user already exists ')
    else:
       password = input('enter the password')
       confirm_passwd = input('confirm password')
       print('registerd successfully!!!')
    
# Existing User Login
if choice == "2":
    email = input("Enter your email: ")
    password = input("enter your password")
    if email in users and email == users:
        print("login sucessfull")
    else:
      print("invalid username/password")
else:
    print("invalid choice")


    
