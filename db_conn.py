import psycopg2

class DBStore(object):
    """For Communicating with DB"""

    __instance = None

    def __init__(self):
        raise Exception("Singleton Class! Please use getInstance() method")

    @staticmethod
    def getInstance():
        if DBStore.__instance == None:
            __instance = psycopg2.connect(host = 'ec2-54-247-177-254.eu-west-1.compute.amazonaws.com', database = 'd273edihuvjs5m' , user = 'sykamvmspiswxh' , password = '455148df3dea0ba4194476a5ee9c91034a202d50a50f71ed8fd7d669dc2dd74e', port = '5432')
        return __instance
