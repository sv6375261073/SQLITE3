#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import sqlite3
#generating random numbers


# In[14]:


r=0
data = (
    (r, 'chrome'))
print(data)

#creating database
conn = sqlite3.connect('database.db')
c = conn.cursor()
#creating table if not exists
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS new_demo1(COUNT INTEGER PRIMARY KEY AUTOINCREMENT,random_no INT, file_name TEXT)')
    conn.commit()
    #inserting values to the DB
def data_entry(key,val):
    data=(key,val)
    c.execute('INSERT INTO new_demo1(random_no,file_name) VALUES(?,?)',data)
    conn.commit()
   

#reading from the DB
def read_from_db():
    c.execute('SELECT * FROM new_demo1')
    data = c.fetchall()
    print(data)
    data =data[-1]
    out = [x for x in data]    
    return (out[0])
def drop_rows(p_key):
    c.execute("""DELETE FROM new_demo1 WHERE COUNT={}""".format(p_key))  # DELETE FROM employees WHERE employeeID = 3;
    conn.commit()
    return -1


# In[15]:


values=['apple','guaua','milk','butter','white','black']
create_table()
# for i,j in enumerate(values):
#     data_entry(i,j)
last_ID=read_from_db()  


# In[16]:


L_pkey=last_ID   # getting last primary key from table 
n=int(input("Enter no of rows to delete from table from end "))
for i in range(n):
    print(drop_rows(L_pkey-i))
    


# In[17]:


last_ID=read_from_db()

