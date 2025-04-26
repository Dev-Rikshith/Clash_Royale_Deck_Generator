import sqlite3
import pandas as pd

def main():
    extract_data()
    # transform_data()

def extract_data():
    
    #Reading the data
    data = pd.read_csv('datasets/clash_royale_cards.csv')
    data1 = pd.read_csv('datasets/clash_wiki_dataset.csv')

    #Merging Columns from both tables
    merged_data = pd.merge(data, data1, on='Card', how='outer')

    transform_data(merged_data)

def transform_data(transformed_data):
    #Cleaning Data
    rows, columns = transformed_data.shape;

    transformed_data = transformed_data.dropna(axis=1, thresh =0.7*columns)
    transformed_data = transformed_data.drop(columns=['id','Cost','Level','Count'])
    transformed_data =  transformed_data

    cols_to_fill = [
    'maxLevel', 'elixirCost', 'rarity', 'Win Rate', 'Win Rate Change', 'Usage', 'Usage Change',
    'Damage', 'Damage per second', 'Health (+Shield)', 'Hit Speed', 'Range', 'Type'
    ]

    # Fill these columns with mean
    for col in cols_to_fill:
        if transformed_data[col].dtype in ['float64', 'int64']:
            transformed_data[col].fillna(transformed_data[col].mean(), inplace=True)
        else:
            transformed_data[col].fillna(transformed_data[col].mode()[0], inplace=True)  # In case of 'Type' being object/string

    # Special case: Death Damage → fill missing values with 0
    transformed_data['Death Damage'].fillna(0, inplace=True)

    transformed_data.to_csv("datasets/final_data.csv")


    print(rows, columns)
    # print(data)
    # print(data1)
    # print(merged_data.columns)
    print(transformed_data)
    # print(merged_data.columns)
    print(transformed_data.isna().sum())
    # print(pd.DataFrame(merged_data))

    load_data(transformed_data)

def load_data(data_to_load):

    conn = sqlite3.connect('clash_royale.db')

    data_to_load.to_sql('cards_table', conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

main()