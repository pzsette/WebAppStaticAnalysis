# MYSQL
mysql_db_username = 'root'
mysql_db_password = 'root'
mysql_db_name = 'bank2'
mysql_db_port = '8889'
mysql_db_hostname = '127.0.0.1'

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "SOME SECRET"

SQLALCHEMY_DATABASE_URI = "mysql://{DB_USER}:{DB_PASS}@{DB_ADDR}:{DB_PORT}/{DB_NAME}".format(
                                                                                    DB_USER=mysql_db_username,
                                                                                    DB_PASS=mysql_db_password,
                                                                                    DB_ADDR=mysql_db_hostname,
                                                                                    DB_PORT=mysql_db_port,
                                                                                    DB_NAME=mysql_db_name)
