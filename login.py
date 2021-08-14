#VIEW OR UI PRESENTETION LOGIC
from users import users
from acountController import acount
from getpass import getpass



def login():
    user=users()


    user.setUsername(input("pleas enter user name:"))
    user.setPassword(getpass())

    myacount=acount()
    myacount.login(user)
    print(user.getMessage())

