user_e = input("enter your new user: ")
password_e = input("enter your new password: ")
print(f"your new user and password: {user_e} {password_e}")

print("log in: READ THIS!!! dont mess up your user and password or else you wont be able to try again sorry for this inconvenience but technology is new and still developing! 🙂")

user = input("enter your user: ")

while user != user_e:
    user = print("sorry but you messed up your user, cant try again ☹️")

password = input("enter your password: ")

while password_e != password:
    password_e = input("sorry but you messed up your password, cant try again ☹️")

print("logged in sueccesfully! 😁")