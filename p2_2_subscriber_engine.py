import pandas as pd
import numpy as np
import os

def generate_subscriber_logs():
    print("--- Phase 2.2: Initializing Subscriber Intelligence Engine (Expanded Devices) ---")
    
    output_dir = 'data'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_file = os.path.join(output_dir, 'NE_Sub_Billing_P2_2.csv')
    
    TOTAL_SUBS = 525000
    DISTRIBUTION = {
        "Bauchi Metro": 0.50, # Urban
        "Alkaleri": 0.35,     # Semi-Urban
        "Kirfi": 0.15         # Rural
    }
    
    subscriber_list = []

    for lga, weight in DISTRIBUTION.items():
        count = int(TOTAL_SUBS * weight)
        print(f"-> Generating {count:,} records for {lga}...")

        # 1. ARPU Modeling (Revenue from calls/data)
        mean_spend = 6000 if lga == "Bauchi Metro" else 2000
        arpu_vals = np.random.lognormal(mean=np.log(mean_spend), sigma=0.6, size=count).round(2)

        # 2. Device Strategy (Expanded with Tecno, Itel, and Feature Phones)
        if lga == "Bauchi Metro":
            devices = ['iPhone 15', 'Samsung S23', 'Tecno Camon', 'Infinix Note', 'Itel S23', 'Feature Phone']
            dev_probs = [0.25, 0.25, 0.15, 0.15, 0.10, 0.10]
            data_scale = 12 
        else:
            devices = ['Feature Phone', 'Itel A58', 'Tecno Pop', 'Infinix Hot', 'Samsung S23', 'Nokia 105']
            # Higher probability of Feature Phones in Rural/Semi-Urban
            dev_probs = [0.45, 0.20, 0.15, 0.10, 0.02, 0.08]
            data_scale = 4

        # 3. Optimized ID Generation
        ids = np.random.randint(7000000000, 9999999999, size=count, dtype=np.int64)
        sub_ids = "234" + pd.Series(ids).astype(str)

        # 4. Initial Data Generation
        data_usage = np.random.exponential(scale=data_scale, size=count).round(2)
        device_choices = np.random.choice(devices, size=count, p=dev_probs)

        # 5. Feature Phone Logic: Zero Data Usage
        # If device is a Feature Phone or Nokia 105, data usage is 0
        df_lga = pd.DataFrame({
            'SubscriberID': sub_ids,
            'LGA_Location': lga,
            'ARPU': arpu_vals,
            'Data_Usage_GB': data_usage,
            'Device_Type': device_choices,
            'Tenure_Months': np.random.randint(1, 72, size=count)
        })

        # Apply the 'No Data' rule for feature phones
        no_data_devices = ['Feature Phone', 'Nokia 105']
        df_lga.loc[df_lga['Device_Type'].isin(no_data_devices), 'Data_Usage_GB'] = 0.00

        subscriber_list.append(df_lga)

    # 6. Final Consolidation
    print("Consolidating all segments...")
    master_subs = pd.concat(subscriber_list, ignore_index=True)
    master_subs.to_csv(output_file, index=False)
    
    print(f"\nSUCCESS: Created {len(master_subs):,} total records.")
    print("--- Device & Data Audit ---")
    print(master_subs.groupby('Device_Type')['Data_Usage_GB'].mean().sort_values())
    print(f"\nFile Saved: {output_file}")

if __name__ == "__main__":
    generate_subscriber_logs()