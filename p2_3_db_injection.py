import pandas as pd
import mysql.connector
from mysql.connector import Error
import time
import os

def connect_to_mysql():
    """Establishes connection to MySQL Server"""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Osita12345' # Ensure this matches your MySQL password
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def run_etl_pipeline():
    conn = connect_to_mysql()
    if not conn: return
    
    cursor = conn.cursor()
    
    # 1. DESIGN: Create Schema
    cursor.execute("CREATE DATABASE IF NOT EXISTS telco_optima_db")
    cursor.execute("USE telco_optima_db")
    
    # 2. DESIGN: Refresh Subscriber Table
    # This 'Drops' the old table so we don't have duplicate or outdated data
    cursor.execute("DROP TABLE IF EXISTS subscribers")
    cursor.execute("""
        CREATE TABLE subscribers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            SubscriberID VARCHAR(20),
            LGA_Location VARCHAR(50),
            ARPU FLOAT,
            Data_Usage_GB FLOAT,
            Device_Type VARCHAR(50),
            Tenure_Months INT
        )
    """)
    print("Database Schema 'telco_optima_db' refreshed and initialized.")

    # 3. EXTRACT: Load the NEW expanded CSV
    file_path = 'data/NE_Sub_Billing_P2_2.csv'
    try:
        # Load the full 525k records
        df = pd.read_csv(file_path)
        print(f"Extracted {len(df):,} records from {file_path}.")
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please run Phase 2.2 first.")
        return

    # 4. LOAD: Batch Injection
    # 10,000 records per batch is the 'sweet spot' for speed and stability
    batch_size = 10000
    sql = "INSERT INTO subscribers (SubscriberID, LGA_Location, ARPU, Data_Usage_GB, Device_Type, Tenure_Months) VALUES (%s, %s, %s, %s, %s, %s)"
    
    print(f"Starting injection into MySQL...")
    start_time = time.time()
    
    try:
        for i in range(0, len(df), batch_size):
            batch = df.iloc[i:i+batch_size]
            # Convert dataframe chunk to list of tuples for SQL injection
            values = [tuple(x) for x in batch.values]
            cursor.executemany(sql, values)
            conn.commit()
            if (i + batch_size) % 50000 == 0:
                print(f"Progress: {i + batch_size:,} / {len(df):,} records loaded...")

        end_time = time.time()
        print(f"\nSUCCESS: ETL Injection Complete!")
        print(f"Total time: {round(end_time - start_time, 2)} seconds.")
        
    except Error as e:
        print(f"Error during injection: {e}")
    
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    run_etl_pipeline()