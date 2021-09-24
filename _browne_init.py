import os


def install():
    print("Welcome to the PyBrowne setup!")

    pb_name = input("Please input the name for your PyBrowne (e.g. My-PyBrowne): ")
    admin_name = input("Please input the name for the admin(no @s or /s please!): ")
    if not '@' in admin_name and not '@' in admin_name:
        admin_pass = input("Please input the password for the admin(no @s or /s please!): ")
        if not '@' in admin_pass and not '/' in admin_pass:

            with open("data.lock", "x") as data:
                data.write(str(pb_name) + '\n' + str(admin_name) + '@' + str(admin_pass))
            with open("installed.lock", 'r+') as installed:
                installed.write('1')
                installed.close()
            
    

    



with open("installed.lock", 'r+') as item:
    if '0' and not '1' in item.read():
        install()
    else:
        os.system("python3 PyBrowne/Main/cmd.py")