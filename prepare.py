import pandas as pd
import numpy as np
import os
from env import host, user, password

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from scipy import stats

def clean_telco(df):
    df.total_charges.replace(to_replace = {" ":"0"}, inplace = True) #Replaces 'blanks' with 0 inside total_charges
    df.total_charges = df.total_charges.astype("float") # Changes total_charges to float type

    pd.set_option("display.max_columns", None) # Allows notebook to display all columns in output

    df["auto_pay"] = df.payment_type.str.contains("auto") # Looks for 'auto' string in payment_type
    df["auto_pay"] = df.auto_pay.replace(to_replace = [True,False],value = [1,0]) # Replaces True with 1 and False with 0

    dummy_df = pd.get_dummies(df[['gender',"internet_service_type","contract_type"]]) # Creates dummies
    dummy_df.drop(columns=['gender_Female'], inplace=True) # Drops gender_Female column
    df = pd.concat([df, dummy_df], axis=1) # Combines dataframes horizontally
    # Encoding (Replaced Yes and No for 1 and 0)
    df["partner"] = df.partner.replace(to_replace = ["Yes","No"],value = [1,0])
    df["dependents"] = df.dependents.replace(to_replace = ["Yes","No"],value = [1,0])
    df["phone_service"] = df.phone_service.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["multiple_lines"] = df.multiple_lines.replace(to_replace = ["Yes","No","No phone service"],value = [1,0,0])
    df["online_security"] = df.online_security.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["online_backup"] = df.online_backup.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["device_protection"] = df.device_protection.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["tech_support"] = df.tech_support.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["streaming_tv"] = df.streaming_tv.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["streaming_movies"] = df.streaming_movies.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["paperless_billing"] = df.paperless_billing.replace(to_replace = ["Yes","No","No internet service"],value = [1,0,0])
    df["churn"] = df.churn.replace(to_replace = ["Yes","No"],value = [1,0])
    # Created new column called "add_ons" which states whether extra features are present
    df["add_ons"] =  ((df.online_security + df.online_backup + df.device_protection + df.tech_support + df.streaming_tv + df.streaming_movies) > 0) 
    df["add_ons"] = df.add_ons.replace(to_replace = [True, False],value = [1,0])
    # Dropped columns I deemed unnecessary
    df = df.drop(columns= ['payment_type_id', 'internet_service_type_id', 'contract_type_id', 'customer_id', 'gender', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'contract_type', 'internet_service_type', 'payment_type'])
    return df



def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test


def churn_pred_csv():
    df = acquire.get_telco_data()
    merged = X_test.merge((df.customer_id), left_index=True, right_index=True, how='left')
    customer_id = merged.customer_id
    probability = pd.DataFrame(y_pred_proba, columns= ['no_churn_prob', 'churn_prob'])
    prediction = pd.DataFrame(y_predictions, columns= ['churn_pred'])
    final_pred = pd.concat([probability, prediction], axis=1)

    customer = pd.DataFrame(customer_id)
    customer.reset_index(drop=True, inplace=True)
    final = pd.concat([final_pred, customer], axis=1)
    final["churn_pred"] = final.churn_pred.replace(to_replace = [1, 0],value = ["Yes","No"])

    return final.to_csv('churn_predictions_df.csv')

