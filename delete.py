#VIEW 

from users import users
from acountController import acount 
import getpass

def delete():
    user=users()
    myacount=acount()


    print(">>>>>> login to delete acount")
    user.setUsername(input("input your user name:"))
    user.setPassword(getpass.getpass())

    myacount.remove(user)
    print(user.getMessage())


