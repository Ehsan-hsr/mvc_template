from users import users
from acountController import acount




def register():
    user=users()

    print(">>>>>>complect form to sign up")
    user.setUsername(input("input your user name:"))
    user.setPassword(input("input your password:"))
    user.setFname(input("input your first name:"))
    user.setLname(input("input your last name:"))
    user.setEmail(input("input your Email:"))



    ac=acount()
    ac.save(user)
    print(user.getMessage())








