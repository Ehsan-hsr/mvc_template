#dbcontex :DB conection
import mysql.connector


class MySql:
    message=""

    try:
        @staticmethod
        def connect():
            connection=mysql.connector.connect(
                    host = "localhost",
                    user = "ehsan",
                    password = "",
                    database = "MVC_DATA")
            if connection.is_connected():
                MySql.message="Connected"
                return connection
    except Exception as e:
        mysql.message=e
    
    @staticmethod
    def disconnect(connection):
        connection.close()
        MySql.message = "connection closed"

