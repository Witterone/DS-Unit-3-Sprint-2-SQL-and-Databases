# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:37:34 2020

@author: Ronin
"""

import pymongo

client = pymongo.MongoClient("mongodb+srv://BW_user:HLc3LQ4PZVDV4KII@cluster0.nrjfe.mongodb.net/test")

db = client.test
#%%


db
db.test

#%%
db.test.insert_one({'x': 1})
db.test.count_documents({'x': 1})
#%%
db.test.find_one({'x': 1})
curs = db.test.find({'x': 1})
list(curs)

#%%
import sqlite3
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

get_characters = 'SELECT * FROM charactercreator_character;'
characters = sl_curs.execute(get_characters).fetchall()
#%%

characters[0]
#%%
for character in characters:
  rpg_character_doc = {
    'doc_type': 'rpg_character',
    'sql_key': character[0],
    'name': character[1],
    'level': character[2],
    'exp': character[3],
    'hp': character[4],
    'strength': character[5],
    'intelligence': character[6],
    'dexterity': character[7],
    'wisdom': character[8]
  }
  db.test.insert_one(rpg_character_doc)
  #%%
  list(db.test.find({'doc_type': 'rpg_character'}))
