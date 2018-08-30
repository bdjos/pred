# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 11:11:56 2018

@author: BJoseph
"""
import pandasdb

db_name = 'bjos'
table_name = 'forecast'
host = '167.99.178.209'

db = pandasdb.pandasdb(db_name, table_name, host)
df = db.pd_from_db()

print(df)