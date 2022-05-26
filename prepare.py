import pandas as pd 
import numpy as np
import os
from env import get_db_url
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer



def clean_iris(df):

    '''Prepares acquired Iris data for exploration'''
    
    # drop column using .drop(columns=column_name)
    df = df.drop(columns='species_id')
    
    # remame column using .rename(columns={current_column_name : replacement_column_name})
    df = df.rename(columns={'species_name':'species'})
    
    # create dummies dataframe using .get_dummies(column_name,not dropping any of the dummy columns)
    dummy_df = pd.get_dummies(df['species'], drop_first=False)
    
    # join original df with dummies df using .concat([original_df,dummy_df], join along the index)
    df = pd.concat([df, dummy_df], axis=1)
    
    return df


def split_iris_data(df):
    '''
    take in a DataFrame and return train, validate, and test DataFrames; stratify on species.
    return train, validate, test DataFrames.
    '''
    
    # splits df into train_validate and test using train_test_split() stratifying on species to get an even mix of each species
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.species)
    
    # splits train_validate into train and validate using train_test_split() stratifying on species to get an even mix of each species
    train, validate = train_test_split(train_validate, 
                                       test_size=.3, 
                                       random_state=123, 
                                       stratify=train_validate.species)
    return train, validate, test


def prep_iris(df):
    '''Prepares acquired Iris data for exploration'''
    
    # drop column using .drop(columns=column_name)
    df = df.drop(columns='species_id')
    
    # remame column using .rename(columns={current_column_name : replacement_column_name})
    df = df.rename(columns={'species_name':'species'})
    
    # create dummies dataframe using .get_dummies(column_name,not dropping any of the dummy columns)
    dummy_df = pd.get_dummies(df['species'], drop_first=False)
    
    # join original df with dummies df using .concat([original_df,dummy_df], join along the index)
    df = pd.concat([df, dummy_df], axis=1)
    
    # split data into train/validate/test using split_data function
    train, validate, test = split_iris_data(df)
    
    return train, validate, test




    ############## TELCO DATA PREPARE#########
def new_telco_data():
    '''
    This function reads the telco data and turns it into a dataframe.
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
      reads telco data, caches it to a local file if there is not one, and returns a df
    '''
    if os.path.isfile('telco.csv'):
        
        # If there is a csv file read the data.
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        df = new_telco_data()
        
        # Cache data if there is not a csv file already
        df.to_csv('telco.csv')
        
    return df


def split_telco_data(df):
  
        train_validate, test = train_test_split(df, test_size= .2, 
                                                    random_state= 123, 
                                                    stratify=df.churn)
        train, validate = train_test_split(train_validate, test_size= .2, 
                                                            random_state= 123, 
                                                            stratify= train_validate.churn)
        return train, validate, test


def tenure_binned(i):
    if i['tenure'] < 6: 
        return"1 - 5"
    elif i['tenure'] > 5 and i['tenure'] < 11:
        return "6 - 10"
    elif i['tenure'] > 10 and i['tenure'] <16:
        return "11 - 15"
    elif i['tenure'] > 15 and i['tenure'] < 21:
        return "16 - 20"
    elif i['tenure'] > 20 and i['tenure']< 26:
        return "21 - 25" 
    elif i['tenure'] >25 and i['tenure']<31: 
        return"26 - 30" 
    elif i['tenure'] >30 and i['tenure']< 36: 
        return "31 - 35" 
    elif i['tenure'] >35 and i['tenure']< 41: 
        return "36 - 40" 
    elif i['tenure'] >40 and i['tenure']< 46: 
        return "41 - 45" 
    elif i['tenure'] >45 and i['tenure']< 51: 
        return "46 - 50" 
    elif i['tenure'] >50 and i['tenure']< 56: 
        return "51 - 55" 
    elif i['tenure'] >55 and i['tenure']< 61: 
        return "56 - 60" 
    elif i['tenure'] >60 and i['tenure']< 66: 
        return "61 - 65" 
    elif i['tenure'] >65 and i['tenure']< 71: 
        return "66 - 70" 
    elif i['tenure'] >70:
        return"71+" ;



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
    
        df['tenure_binned'] = df.apply(lambda x: tenure_binned(x), axis = 1)
        
        train, validate, test = split_telco_data(df)
       
        return train, validate, test

     



def wrangle_telco():
    df = get_telco_data()
    df = prep_telco_data(df)
    return df



def model_telco_data(df):
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
    
        df['tenure_binned'] = df.apply(lambda x: tenure_binned(x), axis = 1)
        
       
        return df


    ########### Titanic Data ############

def clean_titanic_data(df):

    df = df.drop_duplicates()

 
    df = df.drop(columns = ['class' , 'deck', 'embarked'], axis = 1)

    df['embark_town'] = df.embark_town.fillna(value = 'Southampton')

    dummy_df = pd.get_dummies(df[['sex' , 'embark_town']], dummy_na = False, drop_first = [True, True])
    df = pd.concat([df, dummy_df] , axis = 1)

    return df 




def split_titanic_data(df):
  
    # Creates the test set
    train, test = train_test_split(df, test_size = .2, random_state=123, stratify=df.survived)
    
    # Creates the final train and validate set
    train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train.survived)
    
    return train, validate, test





def impute_titanic_mode(train, validate, test):
   
    imputer = SimpleImputer(missing_values = np.nan, strategy='most_frequent')
    train[['embark_town']] = imputer.fit_transform(train[['embark_town']])
    validate[['embark_town']] = imputer.transform(validate[['embark_town']])
    test[['embark_town']] = imputer.transform(test[['embark_town']])
    return train, validate, test

def impute_mean_age(train, validate, test):
  
    # create the imputer object with mean strategy
    imputer = SimpleImputer(strategy = 'mean')
    
    # fit on and transform age column in train
    train['age'] = imputer.fit_transform(train[['age']])
    
    # transform age column in validate
    validate['age'] = imputer.transform(validate[['age']])
    
    # transform age column in test
    test['age'] = imputer.transform(test[['age']])
    
    return train, validate, test



def prep_titanic_data(df):
  
    df = clean_titanic_data(df)

    train, validate, test = split_titanic_data(df)
    
    train, validate, test = impute_mean_age(train, validate, test)

    return train, validate, test







