# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:00:29 2020

@author: Ronin
"""

import psycopg2

dbname = 'nidnwrpi'

user = 'nidnwrpi'

password = 'SfFTOS3EQqsV1c4RKQZEtU7O2g8Kic-9'

host = 'ruby.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

pg_curs = pg_conn.cursor()

create_table_statement = """
CREATE TABLE test_table(
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    data JSONB
    );
"""

#pg_curs.execute(create_table_statement)
#pg_conn.commit()

insert_statement = """
INSERT INTO test_table (name, data) VALUES
(
 'a row name',
 null
 
 ),
(
 'Another row, with JSON this time',
 '{ "a": 1,"b":["dog","cat","moose"],"c": true }'::JSONB
 )

"""

"""
Getting RPG data out of the sqlite3 into PostgreSQL
Our first online ETL
"""
pg_curs.execute(insert_statement)
pg_conn.commit()

query = 'SELECT * FROM test_table'
pg_curs.execute(query)

pg_curs

pg_curs.fetchall()
#%%
import sqlite3
sl_con = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_con.cursor()

get_charaacters = 'SELECT * FROM charactercreator_character;'

characters = sl_curs.execute(get_charaacters).fetchall()

len(characters)

sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()

#%%
create_character_table = """
CREATE TABLE charactercreator_character (
  character_id SERIAL PRIMARY KEY,
  name VARCHAR(30),
  level INT,
  exp INT,
  hp INT,
  strength INT,
  intelligence INT,
  dexterity INT,
  wisdom INT
);
"""
pg_curs.execute(create_character_table)
pg_conn.commit()


example_insert = """
INSERT INTO charactercreator_character
(name,level, exp, hp, str, int, dex, wis),
VALUES """ + str(characters[0][1:]) + ';'

print(example_insert)

for character in characters:
  insert_character = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
  pg_curs.execute(insert_character)
  
pg_curs.execute("""SELECT * FROM charactercreator_character LIMIT 5;""")
pg_characters = pg_curs.fetchall()

pg_conn.commit()


