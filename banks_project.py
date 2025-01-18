# banks_project.py

import requests
import pandas as pd
import sqlite3
import numpy as np
from bs4 import BeautifulSoup
from datetime import datetime

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    with open("code_log.txt", "a") as log_file:
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"{time_stamp} : {message}\n")

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})  # Adapt the class as necessary

    rows = table.find_all('tr')
    data = []
    for row in rows[1:11]:  # Top 10 banks
        cols = row.find_all('td')
        data.append({
            'Name': cols[1].text.strip(),
            'MC_USD_Billion': float(cols[2].text.strip().replace(',', '').replace('$', '').replace(' billion', '').strip())
        })

    df = pd.DataFrame(data)
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    
    exchange_rates = pd.read_csv(csv_path)
    rates = exchange_rates.set_index('Currency')['Rate'].to_dict()
    
    df['MC_GBP_Billion'] = (df['MC_USD_Billion'] / rates['GBP']).round(2)
    df['MC_EUR_Billion'] = (df['MC_USD_Billion'] / rates['EUR']).round(2)
    df['MC_INR_Billion'] = (df['MC_USD_Billion'] * rates['INR']).round(2)

    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    
    df.to_csv(output_path, index=False)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    
    cursor = sql_connection.cursor()
    cursor.execute(query_statement)
    results = cursor.fetchall()
    
    # Get column names from the cursor description
    column_names = [description[0] for description in cursor.description]
    
    # Print column names
    print(f"\nResults for query: {query_statement}\n")
    print(", ".join(column_names))  # Print header
    print("-" * 50)  # Separator
    
    # Print results
    for row in results:
        print(", ".join(str(value) for value in row))
    print("\n" + "=" * 50 + "\n")  # Separator for next query results

# Here, you define the required entities and call the relevant functions in the correct order to complete the project.

# Initializing known values
url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
exchange_rate_csv_path = "exchange_rate.csv"
output_csv_path = "./Largest_banks_data.csv"
database_name = "Banks.db"
table_name = "Largest_banks"

# Logging progress
log_progress("Les préliminaires sont terminés. Lancement du processus ETL")

# Extracting data
df = extract(url, ['Name', 'MC_USD_Billion'])
#print(df)
log_progress("Extraction des données terminée. Lancement du processus de transformation")

# Transforming data
df_transformed = transform(df, exchange_rate_csv_path)
#print(df_transformed)
#print(df_transformed['MC_EUR_Billion'][4])#169.8
log_progress("Transformation des données terminée. Lancement du processus de chargement")

# Loading to CSV
load_to_csv(df_transformed, output_csv_path)
log_progress("Données enregistrées dans un fichier CSV")

# Loading to Database
sql_connection = sqlite3.connect(database_name)
log_progress("Connexion SQL initiée")

load_to_db(df_transformed, sql_connection, table_name)
log_progress("Données chargées dans la base de données sous forme de table, exécution de requêtes")

# Running additional queries
run_query("SELECT * FROM Largest_banks", sql_connection)  # Récupérer toutes les données
run_query("SELECT AVG(MC_GBP_Billion) FROM Largest_banks", sql_connection)  # Calculer la moyenne
run_query("SELECT Name FROM Largest_banks LIMIT 5", sql_connection)  # Limiter à 5 résultats

log_progress("Processus terminé")

# Closing the connection
sql_connection.close()
log_progress("Connexion au serveur fermée")

# Closing the connection
sql_connection.close()
log_progress("Connexion au serveur fermée")
