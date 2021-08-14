
from dbContex import MySql


class acount:

    __connection=""
    def __init__(self):
        self.__connection = MySql.connect()
    
#registeration
    def save(self,user):
        if self.__is_valid(user):
            if self.__save_to_database(user):
                user.setMessage("welcom you are successfully registered")
                return True
        user.setMessage("your data is invalid")
        return False
    def __save_to_database(self,user):
        try:
            cursor = self.__connection.cursor()
            query = f"INSERT INTO `USERS` (`username`,`password`,`fname`,`lname`,`email`) VALUES  ('"+user.getUsername()+"','"+user.getPassword()+"','"+user.getFname()+"','"+user.getLname()+"','"+user.getEmail()+"');"
            cursor.execute(query)
            self.__connection.commit()
            return True
        except Exception as e:
            user.setMessage(e)
            return False

        
    def __is_valid(self,user):
        if (user.getUsername() != "" and
            user.getPassword() != "" and
            user.getFname() != "" and
            user.getLname() != "" and
            user.getEmail() != ""):
            return True
        return False


#loggin
    def login(self,user):
        if self.__is_valid_login(user):
            if self.__is_authorized(user):
                self.__authorize(user)
                return True
            else:
                user.setMessage("your user name or password is Incorrect")
        return False

    def __is_valid_login(self,user):
        if(user.getUsername() !="" and user.getPassword() != ""):
            return True
        return False
    def __is_authorized(self,user):
        cursor=self.__connection.cursor()
        cursor.execute("SELECT `id` FROM `USERS` WHERE `username`='"+user.getUsername()+"' AND `password` ='"+user.getPassword()+"'")
        record = cursor.fetchone()
        if record:
            return True
        return False
    def __authorize(self,user):
        user.setMessage("welcom you are loggined")


#REMOVE USER

    def remove(self,user):
        if self.__is_valid_login(user):
            if  self.__is_authorized(user):
                if self.__del_from_db(user):
                    user.setMessage("bye")
                    return True
        return False

    def __del_from_db(self,user):
        try:
            cursor = self.__connection.cursor()
            query = f"DELETE FROM USERS WHERE username ='"+user.getUsername()+"' AND password='"+user.getPassword()+"';"
            print(query)
            cursor.execute(query)
            self.__connection.commit()
            return True
        except Exception as e:
            user.setMessage(e)
            return False
    def change_password(self,user,newpass):
        if self.__is_valid_login(user):
            if self.__is_authorized(user):
                if self.__update_pass_db(user,newpass):
                    user.setMessage("your password changed successfully")
                    return True
        user.setMessage("there is problem")
        return False

    def __update_pass_db(self,user,newpass):
        try:
            cursor = self.__connection.cursor()
            query = f"UPDATE USERS SET `password` ='{newpass}' WHERE `username`='{user.getUsername()}';"
            cursor.execute(query)
            self.__connection.commit()
            return True
        except Exception as e:
            return False
