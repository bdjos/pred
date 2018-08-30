# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:28:26 2018

@author: BJoseph
"""

import pandasdb
import accuweathertest
import predict
import os

db_name = 'bjos'
table_name = 'forecast'
host='localhost'

df = predict.predict()
print(df.columns)
df_dtypes = ['int', 'int', 'int', 'int', 'int', 'int', 'int', 'int', 'float']

db = pandasdb.pandasdb(db_name, table_name, host)
db.pd_to_db(df_dtypes, df, if_exists='append')

