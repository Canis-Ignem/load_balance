import sqlite3
import pandas as pd



conn = sqlite3.connect('../user_db.db')


def get_sum(user):
    
    res = conn.execute("SELECT md5 from users where user = '{}'".format(user))
    return res.fetchone()[0]

def add_user(user, email, DoB, country, batch ):
    try:
        
        conn.execute("INSERT INTO users (user, email, batch,country, DoB) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(user, email, batch, country, DoB))
        return True
    except:
        return False


def get_batch(user):
    
    res = conn.execute("SELECT batch from users where user = '{}'".format(user))
    
    batch = res.fetchone()
    return str(batch[0])

def get_user(email):
    
    res = conn.execute("SELECT user from users where email = '{}'".format(email))
    
    user = res.fetchone()
    return str(user[0])

def get_email(user):
    
    res = conn.execute("SELECT email from users where user = '{}'".format(user))
    
    email = res.fetchone()
    return str(email[0])



def get_all_users():
    df = pd.read_sql_query("SELECT user from users", conn)
    return df.to_dict()

def get_all_batches():
    df = pd.read_sql_query("SELECT DISTINCT batch from users", conn)
    return df.to_dict()

def update_user(email, args):
    try:
        df = args.dropna()
        value_string =""
        for i in range(df.shape[0]):
            value_string += "{} = '{}',".format(df.index.values[i], df["values"].values[i])
            
        s = "UPDATE users SET {} where email = '{}'".format( value_string[:-1], email)
        conn.execute(s)
        return df.to_dict()
    except:
        return False 


#add_user("jon", "jonperezetxebarria@gmail.com", "1997-08-13", "spain", "Other" )
print(get_all_users())