# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:39:41 2020

@author: Ronin
"""
import sqlite3

import pandas as pd

df = pd.read_csv("C:/Users/Ronin/Documents/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv")
# I needed to include all of the pathing in one line

conn = sqlite3.connect("C:/Users/Ronin/Documents/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv")

df.to_sql("review",conn)

curs = conn.cursor()

row_count = 'SELECT COUNT(*) FROM review;'

print("Total number of entries is ")
print(curs.execute(row_count).fetchall())

nature_shoppers = 'SELECT COUNT(*) FROM review WHERE Nature = 100 AND Shopping = 100;'

print("The number of users who love nature and shopping is ")
print(curs.execute(nature_shoppers).fetchall())

