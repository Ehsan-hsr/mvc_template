#VIEW 

from users import users
from acountController import acount 
import getpass

def change_pass():
    user=users()
    myacount=acount()


    print(">>>>>> change your password")
    user.setUsername(input("input your user name:"))
    user.setPassword(getpass.getpass())

    newpass=input("input your new password:")
    confpass=input("confirm your new password:")


    if newpass == confpass:
        myacount.change_password(user,newpass)
        print(user.getMessage())
    else:
        print("the password and confirmation are diffrent")

