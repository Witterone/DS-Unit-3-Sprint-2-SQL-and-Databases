# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 16:28:31 2020

@author: Ronin
"""
import sqlite3 as sq3

import pandas as pd

import psycopg2

titanic = pd.read_csv('titanic.csv')
#%%
print(titanic.head())


values = titanic.to_records(index=False)
#%%

sq_con = sq3.connect('titanic.sqlite3')

titanic.to_sql("boat", sq_con)

passengers = 'SELECT * FROM boat;'

sq_crs = sq_con.cursor()

query = sq_crs.execute(passengers).fetchall()

#%%
dbname = 'nidnwrpi'

user = 'nidnwrpi'

password = 'SfFTOS3EQqsV1c4RKQZEtU7O2g8Kic-9'

host = 'ruby.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password,
                           host=host)

pg_curs = pg_conn.cursor()

create_titanic_table = """DROP TABLE titanic_table;
CREATE TYPE sex AS ENUM ('male','female');
CREATE TABLE titanic(
    index SERIAL PRIMARY KEY,
    Survived INT,
    Pclass INT,
    Name VARCHAR(100),
    Sex sex,
    Age FLOAT,
    SiblingORSpouse_Aboard INT,
    ParentORChild_Aboard INT,
    Fare FLOAT
    );
"""

pg_curs.execute(create_titanic_table)
pg_conn.commit()
#%%

for people in query:
    insert_passengers = """
    INSERT INTO titanic (Survived, Pclass, Name, Sex, Age,
                         SiblingORSpouse_Aboard, ParentORChild_Aboard,
                         Fare) VALUES """ + str(people[1:])+";"
    pg_curs.execute(insert_passengers)
    
pg_conn.commit()    
