import pandas as pd
import os

def run_data_cleaning():
    print("--- Phase 3.1: Starting Data Cleaning & Audit ---")
    
    # 1. Load the Subscriber Data
    file_path = 'data/NE_Sub_Billing_P2_2.csv'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please run Phase 2.2 first.")
        return
        
    df = pd.read_csv(file_path)
    print(f"Successfully loaded {len(df):,} records for auditing.")

    # 2. Audit for Missing Values
    null_counts = df.isnull().sum()
    if null_counts.sum() > 0:
        print("\n--- Missing Values Found ---")
        print(null_counts[null_counts > 0])
        df = df.dropna() 
        print("Cleanup: Null records removed.")
    else:
        print("\nAudit Pass: No missing values detected.")

    # 3. Handle ARPU Outliers (Capping at 99th Percentile)
    # This ensures extreme spenders don't warp the ML model's logic
    arpu_cap = df['ARPU'].quantile(0.99)
    outlier_count = len(df[df['ARPU'] > arpu_cap])
    df['ARPU'] = df['ARPU'].clip(upper=arpu_cap)
    
    print(f"Outlier Audit: Capped {outlier_count:,} records at ₦{arpu_cap:,.2f} for model stability.")

    # 4. Enforce Logical Consistency
    # Rule A: Active subscribers must have at least 1 month tenure
    df['Tenure_Months'] = df['Tenure_Months'].replace(0, 1)
    
    # Rule B: Voice-Only Audit (Feature Phones should have 0 data usage)
    voice_only_devices = ['Feature Phone', 'Nokia 105', 'Nokia 3310']
    voice_users = df[df['Device_Type'].isin(voice_only_devices)]
    avg_data = voice_users['Data_Usage_GB'].mean()
    
    print(f"Voice-Only Audit: Found {len(voice_users):,} users.")
    if avg_data == 0:
        print("Logic Check Passed: Call-Card users correctly show 0.00 GB usage.")

    # 5. Save the Cleaned Checkpoint
    # We save as .pkl (Pickle) to keep the data types perfect for Phase 3.2
    output_path = 'data/cleaned_subscribers.pkl'
    df.to_pickle(output_path)
    
    print(f"\nSUCCESS: Data Cleaning Complete.")
    print(f"Final Dataset: {len(df):,} rows saved to {output_path}")

if __name__ == "__main__":
    run_data_cleaning()