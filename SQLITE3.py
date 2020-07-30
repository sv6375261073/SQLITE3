#!/usr/bin/env python
# coding: utf-8

# In[318]:


import random
import sqlite3
#generating random numbers


# In[348]:


#creating database
conn = sqlite3.connect('database.db')
c = conn.cursor()
#creating table if not exists
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS new_demo1(COUNT varchar PRIMARY KEY )')
    conn.commit()
    #inserting values to the DB
def data_entry():
    c.execute("""select COUNT from new_demo1""")
    n=len(c.fetchall())+1
#     try:
    c.execute('INSERT INTO new_demo1(COUNT) VALUES(?)',str(n))
    conn.commit()
#     except:
#         pass
   
#reading from the DB
def read_from_db():
    c.execute('SELECT * FROM new_demo1')
    data = c.fetchall()
    print(data)
    try:
        data =data[-1]
        out = [x for x in data]
    except:
          return None
    return (out[0])
def drop_rows():
    c.execute('select count  from new_demo1')
    n=len(c.fetchall())
    c.execute("""DELETE FROM new_demo1 WHERE COUNT BETWEEN {} and {}""".format(n-3,n+1))
    return conn.commit()


# In[320]:


create_table()


# In[365]:


data_entry()


# In[363]:


drop_rows()


# In[366]:


read_from_db()


# In[367]:


# c.execute('drop table new_demo1')
# conn.commit()

