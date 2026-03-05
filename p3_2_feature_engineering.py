import pandas as pd
import numpy as np
import mysql.connector
import os

def run_feature_engineering():
    print("--- Phase 3.2: Starting Feature Engineering (LGA & AI Targets) ---")
    
    # 1. Database Connection to fetch the Propensity_Score
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Osita12345',
            database='telco_optima_db'
        )
        print("Successfully connected to MySQL to fetch AI Labels.")
        
        # Load subscribers with the Propensity_Score we generated in 2.4
        df_subs = pd.read_sql("SELECT * FROM subscribers", conn)
        conn.close()
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")
        return

    # 2. Load Population Data for Penetration Calculation
    pop_path = 'data/population_ground_truth.csv'
    if not os.path.exists(pop_path):
        print(f"Error: {pop_path} not found.")
        return
    df_pop = pd.read_csv(pop_path, usecols=['LGA'])

    # 3. CALCULATION 1: Market Penetration Rate (Territory Level)
    print("Step 1: Calculating Market Penetration Rates...")
    sub_counts = df_subs['LGA_Location'].value_counts()
    pop_counts = df_pop['LGA'].value_counts()
    
    penetration_data = []
    for lga in pop_counts.index:
        s = sub_counts.get(lga, 0)
        p = pop_counts[lga]
        rate = (s / p) * 100
        penetration_data.append({
            'LGA': lga, 
            'Subscribers': s, 
            'Population': p, 
            'Penetration_Rate_%': round(rate, 2)
        })
    df_territory = pd.DataFrame(penetration_data)
    df_territory['Acquisition_Priority'] = pd.qcut(df_territory['Penetration_Rate_%'], 3, labels=["High", "Medium", "Low"])
    
    # 4. CALCULATION 2: High Value Flag
    print("Step 2: Tagging High-Value Customers (ARPU > Mean)...")
    avg_arpu = df_subs['ARPU'].mean()
    df_subs['Is_High_Value'] = (df_subs['ARPU'] > avg_arpu).astype(int)
    
    # 5. Save the Output for Phase 4
    df_territory.to_csv('data/territory_intelligence.csv', index=False)
    # This file NOW includes 'Propensity_Score' from the database
    df_subs.to_pickle('data/enriched_subscribers.pkl')
    
    print("\n--- TERRITORY INTELLIGENCE SUMMARY ---")
    print(df_territory)
    print(f"\nSUCCESS: 'enriched_subscribers.pkl' now contains the 'Propensity_Score'.")

if __name__ == "__main__":
    run_feature_engineering()