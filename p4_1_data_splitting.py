import pandas as pd
from sklearn.model_selection import train_test_split
import os

def run_data_splitting():
    print("--- Phase 4.1: Data Splitting for Machine Learning ---")

    # 1. Load the Enriched Data from Phase 3.2
    file_path = 'data/enriched_subscribers.pkl'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found. Please ensure Phase 3.2 was completed successfully.")
        return

    df = pd.read_pickle(file_path)
    print(f"Successfully loaded {len(df):,} subscriber records.")

    # 2. Feature Selection & Target Definition
    # Target (y): Propensity_Score (1 for high potential lead, 0 for others)
    y = df['Propensity_Score']

    # Features (X): We drop ID and the Target itself.
    # We include 'Is_High_Value' as an engineered feature to help the model learn.
    X = df.drop(['SubscriberID', 'Propensity_Score'], axis=1)

    # 3. Categorical Encoding (One-Hot Encoding)
    # Machine Learning models require numbers. We convert LGA names and Device Types into binary columns.
    print("Encoding categorical variables (LGAs and Device Types)...")
    X = pd.get_dummies(X, columns=['LGA_Location', 'Device_Type'], drop_first=True)

    # 4. Perform the Split (80% Training, 20% Testing)
    # Stratify=y ensures the 1/0 ratio is the same in both sets to maintain balance
    print("Splitting data into 80% Training and 20% Testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    # 5. Save the split data for Step 4.2 (Model Training)
    # We save these as checkpoints in a dedicated folder
    os.makedirs('data/model_data', exist_ok=True)
    X_train.to_pickle('data/model_data/X_train.pkl')
    X_test.to_pickle('data/model_data/X_test.pkl')
    y_train.to_pickle('data/model_data/y_train.pkl')
    y_test.to_pickle('data/model_data/y_test.pkl')

    print(f"\nSUCCESS: Data Splitting Complete.")
    print(f"- Training Samples: {len(X_train):,}")
    print(f"- Testing Samples: {len(X_test):,}")
    print(f"- Target Balance (Propensity Rate): {y_train.mean():.2%}")
    print(f"- Files saved in: data/model_data/")

if __name__ == "__main__":
    run_data_splitting()