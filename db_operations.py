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

def db_read_user_history(user_id,search_like):
    """ To read the USER Search History in DB"""
    query = "SELECT search_string FROM search_history where user_id = {} and ({})"
    try:
        result_str = "Here are your recent related searches : \n\n"
        conn = DBStore.getInstance()
        cur = conn.cursor()
        cur.execute(query.format(user_id,' OR '.join([f"LOWER(search_string) LIKE '%{y}%'" for y in search_like.lower().split()])))
        results = cur.fetchall()
        result_str = result_str + "\n".join([row[0].strip() for row in results])
        return result_str
    except:
        raise Exception("Unable to Read User Search History to DB!")
