import os
import sys
from src.datascienceproject.exception import CustomException
from src.datascienceproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import psycopg2 


load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading Postgre SQL database started")
    try:
        mydb=psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=db
            
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())


        return df 



    except Exception as ex:
        raise CustomException(ex,sys)