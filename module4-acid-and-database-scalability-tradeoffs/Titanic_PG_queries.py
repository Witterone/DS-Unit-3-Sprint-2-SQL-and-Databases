# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:49:37 2020

@author: Ronin
"""



import psycopg2

dbname = 'nidnwrpi'

user = 'nidnwrpi'

password = 'SfFTOS3EQqsV1c4RKQZEtU7O2g8Kic-9'

host = 'ruby.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password,
                           host=host)

pg_curs = pg_conn.cursor()
#%%
Survival = """ SELECT COUNT(*) FROM titanic WHERE "Survived" = 0;
            SELECT COUNT(*) FROM titanic WHERE "Survived" =1;"""
            
print(pg_curs.execute(Survival).fetchall())

#%%
Classify = """ SELECT COUNT("Pclass") FROM titanic GROUP BY "Pclass";"""

print(pg_curs.execute(Classify).fetchall())

#%%
class_war = """ SELECT COUNT(*) FROM titanic WHERE "Survived" = 0 
                GROUP BY "Pclass";
                
                SELECT COUNT(*) FROM titanic WHERE "Survived" = 1
                GROUP BY "Pclass": """
                
print(pg_curs.execute(class_war).fetchall())
#%%

age_survivor = """ SELECT AVG("Age") FROM titanic GROUP BY "Survived";
                    """

print(pg_curs.execute(age_survivor).fetchall())

#%%

age_class = """ SELECT AVG("Age") FROM titanic GROUP BY "Pclass";"""

print(pg_curs.execute(age_class).fetchall())

#%%

fare_averages = """ SELECT AVG("Fare") FROM titanic GROUP BY "Pclass";

                    SELECT AVG("Fare") FROM titanic GROUP BY "Survived";
                    """

print(pg_curs.execute(fare_averages).fetchall())

#%%

survivors_guilt = """ SELECT AVG("SiblingORSpouse_Aboard") FROM titanic 
                    GROUP BY "Pclass", "Survived";
                    
                    SELECT AVG("ParentORChild_Aboard") FROM titanic
                    GROUP BY "Pclass", "Survived";
                    """
                    
print(pg_curs.execute(survivors_guilt).fetchall())

#%%

name_matcher = """ SELECT COUNT(*) FROM titanic WHERE "Name" LIKE "Name";
                """
                
print(pg_curs.execute(name_matcher).fetchall())