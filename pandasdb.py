# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:24:19 2018

@author: BJoseph
"""
import psycopg2
import pandas as pd

class pandasdb():
    def __init__(self, database, table):
        self.database = database
        self.table = table
        
    def pd_to_db(self, dtypes, df, if_exists):
        if len(dtypes) != len(df.columns):
            print('len of dtypes must equal number of columns')
        else:
            dtypes_dict = dict(zip(list(df.columns), dtypes))
        
            connection = psycopg2.connect(host=self.host, database="bjos", user="bjos", password="3iRM7Ihr@")
            df.to_sql(name = self.table, con = connection, if_exists = if_exists, dtype = dtypes_dict)
            connection.close()
        
    def pd_from_db(self):
        connection = psycopg2.connect(host="localhost", database="bjos", user="bjos", password="3iRM7Ihr@")
        
        df = pd.read_sql(f'SELECT * FROM {self.table}', con = connection)
        connection.close()
        
        return df
    