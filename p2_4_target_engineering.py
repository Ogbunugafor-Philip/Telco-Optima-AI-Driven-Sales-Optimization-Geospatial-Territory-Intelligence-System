import pandas as pd
import mysql.connector
from mysql.connector import Error
import numpy as np

def run_target_engineering():
    print("--- Phase 2.4: Refreshing AI Target Variables (Propensity Scoring) ---")
    
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Osita12345',
            database='telco_optima_db'
        )
        cursor = conn.cursor()

        # 1. Add Propensity Column if it doesn't exist
        cursor.execute("SHOW COLUMNS FROM subscribers LIKE 'Propensity_Score'")
        if not cursor.fetchone():
            cursor.execute("ALTER TABLE subscribers ADD COLUMN Propensity_Score INT DEFAULT 0")
            conn.commit()

        # 2. Extract for Labeling
        df = pd.read_sql("SELECT * FROM subscribers", conn)

        # 3. Prescriptive Logic (The 'Answer Key' for the AI)
        # 1 = High Propensity (Target for Sales), 0 = Standard
        print("Applying Logic: Identifying High-Value Power Users...")
        df['Propensity_Score'] = np.where(
            ((df['ARPU'] > 5000) & (df['Data_Usage_GB'] > 10)) | 
            ((df['Tenure_Months'] > 24) & (df['ARPU'] > 4000)),
            1, 0
        )

        # 4. Batch Update MySQL
        update_sql = "UPDATE subscribers SET Propensity_Score = %s WHERE id = %s"
        batch_data = list(zip(df['Propensity_Score'].astype(int), df['id']))
        
        batch_size = 10000
        for i in range(0, len(batch_data), batch_size):
            chunk = batch_data[i:i+batch_size]
            cursor.executemany(update_sql, chunk)
            conn.commit()
            if (i + batch_size) % 50000 == 0:
                print(f"Labeled {i + batch_size:,} records...")

        print("\nSUCCESS: AI Target Variables generated for the new device mix.")
        
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    run_target_engineering()