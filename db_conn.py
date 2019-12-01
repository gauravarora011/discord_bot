import psycopg2
import os

class DBStore(object):
    """For Communicating with DB"""

    __instance = None

    def __init__(self):
        raise Exception("Singleton Class! Please use getInstance() method")

    @staticmethod
    def getInstance():
        if DBStore.__instance == None:
            host = os.environ.get('discordapp_db_host')
            database = os.environ.get('discordapp_db_database')
            user = os.environ.get('discordapp_db_user')
            password = os.environ.get('discordapp_db_password')
            port = os.environ.get('discordapp_db_port')
            #print(host,database,user,password,port)
            __instance = psycopg2.connect(host = host, database = database, user = user, password = password, port = port)
        return __instance
