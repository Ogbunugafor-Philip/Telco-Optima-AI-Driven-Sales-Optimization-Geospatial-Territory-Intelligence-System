import pandas as pd
import numpy as np
import os

def run_opportunity_scoring():
    print("--- Phase 5.3: Generating Territory Priority Scores ---")

    # 1. Load the Delta Analysis Report
    file_path = 'data/delta_analysis_report.csv'
    if not os.path.exists(file_path):
        print("Error: Delta report not found. Please run Phase 5.2 first.")
        return

    df = pd.read_csv(file_path)

    # 2. Weighted Scoring Formula
    # Weight A: Uncaptured Market (40%) - The volume of potential money
    # Weight B: Penetration Gap (40%) - How 'empty' the market is
    # Weight C: Population Density (20%) - The sheer number of people
    
    print("Applying Weighted Opportunity Logic...")
    
    # Normalize values to a 0-1 scale for fair weighting
    uncaptured_norm = (df['Uncaptured_Market'] - df['Uncaptured_Market'].min()) / (df['Uncaptured_Market'].max() - df['Uncaptured_Market'].min())
    gap_norm = (100 - df['Penetration_Rate_%']) / 100 # Higher gap = higher score
    pop_norm = (df['Population'] - df['Population'].min()) / (df['Population'].max() - df['Population'].min())

    # Calculate final score out of 100
    df['Priority_Score'] = (
        (uncaptured_norm * 40) + 
        (gap_norm * 40) + 
        (pop_norm * 20)
    ).round(2)

    # 3. Final Strategic Ranking
    df = df.sort_values(by='Priority_Score', ascending=False)
    
    # Define Action Plan
    df['Recommended_Action'] = np.where(df['Priority_Score'] > 70, "Aggressive Acquisition", 
                               np.where(df['Priority_Score'] > 40, "Steady Expansion", "Retention Focus"))

    # 4. Save Final Strategic Report
    df.to_csv('data/final_territory_strategy.csv', index=False)
    
    print("\n" + "="*50)
    print("      FINAL TERRITORY STRATEGIC RANKING")
    print("="*50)
    print(df[['LGA', 'Uncaptured_Market', 'Priority_Score', 'Recommended_Action']])
    print("="*50)

    print(f"\nSUCCESS: Priority Scoring complete. Saved to 'data/final_territory_strategy.csv'")
    print(f"Top Target: {df.iloc[0]['LGA']} with a score of {df.iloc[0]['Priority_Score']}/100.")

if __name__ == "__main__":
    run_opportunity_scoring()