#view 
from login import login
from delete import delete
from register import register
from change_pass import change_pass



print(">>>>>>>>>>")
print("(l) for login:")
print("(d) for delete:")
print("(r) for register:")
print("(e) for change password:")



q = input("select:")
if q.lower() == "l":
    login()
elif q.lower() == "d":
    delete()
elif q.lower() == "r":
    register()
elif q.lower() == "e":
    change_pass()


print("bye")
