user_name = "taleeb"
user_password = "1234"

while True:
    name = input("enter your username : ")
    password = input("enter your password : ")

    if name == user_name and password == user_password:
        print(f"{user_name} can login successfully")
        break
    else:
        print("username or password is wrong. Try again.")

