import pandas as pd
import numpy as np
import os

def run_delta_calculation():
    print("--- Phase 5.2: Executing Geospatial 'Delta' Algorithm ---")

    # 1. Load the Intelligence datasets
    territory_path = 'data/territory_intelligence.csv'
    if not os.path.exists(territory_path):
        print("Error: Required intelligence file missing. Run Phase 3.2 first.")
        return

    df_stats = pd.read_csv(territory_path)

    # 2. Define the "White Space" Logic
    # We define 'High Population' as > 500k and 'Low Penetration' as < 30%
    print("Analyzing Demographic Gaps...")
    
    # Calculate the Delta: Population minus Subscribers
    df_stats['Uncaptured_Market'] = df_stats['Population'] - df_stats['Subscribers']
    
    # 3. Identify White Spaces via High Density + Low Penetration
    # This identifies where we have many people but few customers
    df_stats['Is_White_Space'] = np.where(
        (df_stats['Population'] > 300000) & (df_stats['Penetration_Rate_%'] < 35),
        "YES - Expansion Target",
        "NO - Saturated/Low Priority"
    )

    # 4. Calculate Market Opportunity Index (MOI)
    # MOI = Uncaptured Market / Population * 100
    df_stats['Market_Opportunity_Index'] = (df_stats['Uncaptured_Market'] / df_stats['Population'] * 100).round(2)

    # 5. Save the Delta Report
    df_stats.to_csv('data/delta_analysis_report.csv', index=False)
    
    print("\n--- DELTA CALCULATION SUMMARY ---")
    # Show the LGAs ranked by the largest uncaptured market
    summary = df_stats[['LGA', 'Population', 'Subscribers', 'Uncaptured_Market', 'Is_White_Space']]
    print(summary.sort_values(by='Uncaptured_Market', ascending=False))
    
    print(f"\nSUCCESS: Delta Analysis saved to 'data/delta_analysis_report.csv'")
    print(f"Insight: {df_stats[df_stats['Is_White_Space'] == 'YES - Expansion Target']['LGA'].tolist()} identified as primary White Spaces.")

if __name__ == "__main__":
    run_delta_calculation()