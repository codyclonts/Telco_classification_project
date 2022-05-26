Project Summary

Project Goal: Identify possible reasons for customer churn in order to make recommendations as to how to minimize churn in the future. 


Initial Hypothesis:

I expect that churn will be primarily affected by:
    - The type of internet that a person uses
    - Age of the customers: senior citizens will be more likely to churn
    -Cost: Customers paying a higher monthly cost will be more likely to churn.

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
