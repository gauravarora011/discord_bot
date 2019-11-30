from db_conn import DBStore
import uuid
import datetime

def db_write_user_ping(user_id):
    """To store the User Ping TimeStamps to DB"""
    query = "INSERT INTO user_ping(uuid,user_id,timestamp) VALUES('{}','{}','{}')"
    try:
        conn = DBStore.getInstance()
        cur = conn.cursor()
        cur.execute(query.format(uuid.uuid1(),user_id,datetime.datetime.now()))
        conn.commit()
    except:
        raise Exception("Unable to Insert User Ping to DB!")

def db_write_user_search(user_id,search_string):
    """ To write the USER Search History in DB"""
    query = "INSERT INTO search_history(uuid,user_id,search_string,timestamp) VALUES('{}','{}','{}','{}')"
    try:
        conn = DBStore.getInstance()
        cur = conn.cursor()
        cur.execute(query.format(uuid.uuid1(),user_id,search_string,datetime.datetime.now()))
        conn.commit()
    except:
        raise Exception("Unable to Insert User Search History to DB!")

def db_read_user_history(user_id,searc_like):
    """ To write the USER Search History in DB"""
    query = "SELECT * FROM search_history WHERE user_id = {} and search_string LIKE '%{}%';"
    try:
        conn = DBStore.getInstance()
        cur = conn.cursor()
        cur.execute(query.format(user_id,searc_like))
        results = cur.fetchall()
        
    except:
        raise Exception("Unable to Insert User Search History to DB!")


if __name__ == '__main__':
    db_read_user_history()
