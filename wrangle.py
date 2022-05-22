from lib2to3.pgen2.pgen import DFAState
import pandas as pd 
import numpy as np 
import os 
from env import get_db_url
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer





# combine acquire and prepare 



def new_telco_data():
    '''
    This function reads the iris data from the Codeup db into a df.
    '''
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    url = get_db_url('telco_churn')
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, url)
    
    return df



def get_telco_data():
    '''
    This function reads in iris data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('telco.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_telco_data()
        
        # Cache data
        df.to_csv('telco.csv')
        
    return df



def prep_telco_data(df):
    #drop columns that aren't necessary 
    
        columns = ['customer_id', 'payment_type_id', 'internet_service_type_id' , 'contract_type_id']
        df.drop(columns, inplace = True, axis = 1)
    
    #fix total charges
    
        df['total_charges'] = df['total_charges'].str.strip()
        df = df[df.total_charges != '']
        df['total_charges'] = df.total_charges.astype(float)
    
    #get dummy variables
        dummy_df = pd.get_dummies(df[['gender', \
                                    'partner', \
                                    'dependents', \
                                    'phone_service', \
                                    'paperless_billing', \
                                    'churn', \
                                    'multiple_lines', \
                                    'online_security', \
                                    'device_protection', \
                                    'tech_support', \
                                    'streaming_tv', \
                                     'streaming_movies', \
                                     'contract_type', \
                                     'internet_service_type', \
                                     'payment_type']], dummy_na=False, \
                                  drop_first=True)
    
        df = pd.concat([df, dummy_df], axis = 1)
    
        return df
     



def wrangle_telco():
    df = get_telco_data()
    df = prep_telco_data(df)
    return df