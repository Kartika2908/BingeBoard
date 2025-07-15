
import pandas as pd
from datetime import datetime
import os

def clean_and_merge(dfs):
    platforms = ['Netflix', 'Amazon Prime', 'Disney+']
    for i, df in enumerate(dfs):
        df['platform'] = platforms[i]
    df = pd.concat(dfs, ignore_index=True)
    df['release_year'] = pd.to_datetime(df['release_year'], errors='coerce').dt.year
    return df

def filter_data(df, platforms, countries, genres):
    if platforms:
        df = df[df['platform'].isin(platforms)]
    if countries:
        df = df[df['country'].isin(countries)]
    if genres:
        df = df[df['listed_in'].isin(genres)]
    return df

def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def save_contact(name, email, message):
    os.makedirs("contact_data", exist_ok=True)
    data = pd.DataFrame([[datetime.now(), name, email, message]],
                        columns=["timestamp", "name", "email", "message"])
    if os.path.exists("contact_data/contacts.csv"):
        data.to_csv("contact_data/contacts.csv", mode='a', header=False, index=False)
    else:
        data.to_csv("contact_data/contacts.csv", index=False)
