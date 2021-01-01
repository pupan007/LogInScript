#Login project
while True:
    question = input("Create new account or Login or Exit? >")
    def create_account():
        user_name = input("Username? >")
        password = input("password? >")
        email = input("Email? >")
        with open("databaza.txt", "a") as file:
            file.write(f"{user_name} {password} {email}\n")


    def login():
        user_name = input("Username? >")
        password = input("Password? >")
        with open("databaza.txt", "r") as file:
            data = file.readlines()
            for line in data:
                user_name1, password1, email = line.split()

                if user_name == user_name1 and password == password1:
                    return True


    if question.lower() == "create":
        create_account()
        print("Accout created! ")
    elif question.lower() == "login":
        if login() == True:
            print("You are logged in! ")
            with open("Status.txt", "w") as file:
                file.write("True")
        else:
            print("Bad username or password!" )
    elif question.lower() == "exit":
        break
    elif question.lower() == "help":
        print("login to log in \n"
              "create to create new account\n"
              "help to show commands\n"
              "logout to log out from your account\n"
              "exit to stop program")
    elif question.lower() == "logout":
        with open("Status.txt", "r") as file:
            status = file.read()
            if status == "True":
                print("You successfully logged out")
                with open("Status.txt", "w") as file:
                    file.write("False")
            else:
                print("You are not logged in ")
    else:
        print("Wrong input")
