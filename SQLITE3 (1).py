#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install sqlite3
import random
import sqlite3
#generating random numbers


# In[15]:


#creating database
conn = sqlite3.connect('database2.db')
c = conn.cursor()

#creating table if not exists
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS table1(COUNT integer PRIMARY KEY autoincrement,
    num1 integer(10),
    num2 integer(10) )"""
             )
    conn.commit()
    c.execute("""CREATE TABLE IF NOT EXISTS table2(COUNT integer PRIMARY KEY autoincrement,
    num1 integer(10),
    num2 integer(10) )"""
             )
    conn.commit()
    
#inserting values to the DB
def data_entry(table1=True):
    if table1==True:
        c.execute('INSERT INTO table1(num1,num2) VALUES(?,?)',(random.randint(0,20),random.choice([6,8])))
        conn.commit()
    else:
        c.execute('INSERT INTO table2(num1,num2) VALUES(?,?)',(random.randint(0,20),random.choice([6,8])))
        conn.commit()

   
#reading from the DB
def read_from_db(table1=True):
    if table1==True:
        c.execute('SELECT * FROM table1')
        data = c.fetchall()
        out = [list(item) for item in list(data)]
        return out
    else:
        c.execute('SELECT * FROM table2')
        data = c.fetchall()
        out = [list(item) for item in list(data)]
        return out


# In[13]:


create_table()


# In[27]:


data_entry(table1=False)


# In[29]:


data1=read_from_db()
print(data1)
data2=read_from_db(table1=False)
print(data2)


# In[367]:


# c.execute('drop table new_demo1')
# conn.commit()

