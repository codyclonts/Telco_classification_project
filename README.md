Project Summary

Project Goals

- Identify possible reasons for customer churn in order to make recommendations as to how to minimize churn in the future. 
- Document code, process, findings, and takeaways 
- create acquire and prepare functions and store them in an overall wrangle function.
- construct machine learning model to predict customer churn

Audience

- Telco stakeholders
- first line supervisor
- fellow codeup students


Initial Hypothesis:

I expect that churn will be driven by:
    - The type of internet that a person uses
    - Age of the customers: senior citizens will be more likely to churn
    - Cost: Customers paying a higher monthly cost will be more likely to churn.
    - Tenure of the customer
    - payment type

Initial Questions: 
    - What factors drive churn? 
    - Is there anything that our company can do to prevent these customers from churning?


Project Plan: 
    - Acquire the data from servers
    - prepare the data 
        - get rid of duplicate columns
        - identify missing data
        - create dummy columns
        - clean the data
    -  make a wrangle function to combine acquire and prepare functions
    - Explore the data:
        - create visuals to more easily identify what may be driving customer churn
        - identify percent of churn
        -run statistical analysis on features that visually appear to drive churn to see if there is statistical significance in these groups. 
    - model the data:
        - create a baseline
        - create minimum of 10 models
        - generate and fit models on the train dataset
        - evaluate which model performed the best based off of preferred model statistics
    -Final report
        -run model against test dataset 
    -Reproduce the project
        -User will need an env.py file with the the following variables: 'host', 'user' (username), and 'password'



Data columns (total 24 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   payment_type_id           7043 non-null   int64  
 1   internet_service_type_id  7043 non-null   int64  
 2   contract_type_id          7043 non-null   int64  
 3   customer_id               7043 non-null   object 
 4   gender                    7043 non-null   object  
 5   senior_citizen            7043 non-null   int64  
 6   partner                   7043 non-null   object 
 7   dependents                7043 non-null   object 
 8   tenure                    7043 non-null   int64  
 9   phone_service             7043 non-null   object 
 10  multiple_lines            7043 non-null   object 
 11  online_security           7043 non-null   object 
 12  online_backup             7043 non-null   object 
 13  device_protection         7043 non-null   object 
 14  tech_support              7043 non-null   object 
 15  streaming_tv              7043 non-null   object 
 16  streaming_movies          7043 non-null   object 
 17  paperless_billing         7043 non-null   object 
 18  monthly_charges           7043 non-null   float64
 19  total_charges             7043 non-null   object 
 20  churn                     7043 non-null   object 
 21  contract_type             7043 non-null   object 
 22  internet_service_type     7043 non-null   object 
 23  payment_type              7043 non-null   object 
dtypes: float64(1), int64(5), object(18)
