# MYSQL
mysql_db_username = 'root'
mysql_db_password = 'root'
mysql_db_name = 'bank2'
mysql_db_hostname = 'localhost'

DEBUG = True
PORT = 5000
HOST = "127.0.0.1"

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "SOME SECRET"

SQLALCHEMY_DATABASE_URI = "mysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
                                                                                    DB_USER=mysql_db_username,
                                                                                    DB_PASS=mysql_db_password,
                                                                                    DB_ADDR=mysql_db_hostname,
                                                                                    DB_NAME=mysql_db_name)
