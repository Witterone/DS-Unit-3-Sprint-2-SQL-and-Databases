# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 12:03:32 2020

@author: Ronin
"""


import sqlite3 

conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

count_characters = 'SELECT COUNT(*) FROM charactercreator_character;'


print("total characters count is "+
      curs.execute(count_characters).fetchall())
#%%
count_clerics = 'SELECT COUNT(*) FROM charactercreator_cleric;'

count_fighters = 'SELECT COUNT(*) FROM charactercreator_fighter;'

count_mages = 'SELECT COUNT(*) FROM charactercreator_mage;'

count_thieves = 'SELECT COUNT(*) FROM charactercreator_thief;'

count_necros = 'SELECT COUNT(*) FROM charactercreator_necromancer;'


print ("The number of clerics is "+
       curs.execute(count_clerics).fetchall())

print("The number of fighters is "+
       curs.execute(count_fighters).fetchall())

print("The number of mages is "+
       curs.execute(count_mages).fetchall())

print("The number of thieves is "+
       curs.execute(count_thieves).fetchall())

print("The number of necromancers is "+
       curs.execute(count_necros).fetchall())

#%%
count_items = 'SELECT COUNT(UNIQUE) FROM armory_item, armory_weapon;'


print("The total number of items is "+
       curs.execute(count_items).fetchall())
    
#%%
count_weapons = 'SELECT COUNT(*) FROM armory_weapon;'
count_sundry = 'SELECT COUNT(*) FROM armory_items;'


print("The number of weapons is "+
      curs.execute(count_weapons).fetchall())

print("The number of non-weapon items is "+
      curs.execute(count_sundry).fetchall())

#%%

character_inventory = '''SELECT COUNT(item_id) 
FROM charactercreator_character_inventory 
GROUP BY character_id LIMIT 20;'''

character_weapons = '''SELECT COUNT(item_id) 
FROM charactercreator_character_inventory 
INNER JOIN armory_weapon 
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY character_id LIMIT 20;'''


print("The first twenty players item counts are "+
      curs.execute(character_inventory).fetchall())
print("The first twenty players weapon counts are "+
      curs.execute(character_weapons).fetchall())
#%%
average_inventory = '''SELECT AVG(COUNT(item_id)) 
FROM charactercreator_character_inventory;'''

average_weapon = '''SELECT AVG(COUNT(item_id)) 
FROM charactercreator_character_inventory
INNER JOIN armory_weapon
ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id;'''


print("The average number of items a player has is "+
        curs.execute(average_inventory).fetchall())

print("The average number of weapons a player has is "+
        curs.execute(average_weapon).fetchall())

