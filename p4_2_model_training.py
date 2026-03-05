import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import time
import os

def run_model_training():
    print("--- Phase 4.2: Training the Random Forest Lead Scoring Model ---")

    # 1. Load the Split Data
    data_dir = 'data/model_data'
    try:
        X_train = pd.read_pickle(f'{data_dir}/X_train.pkl')
        y_train = pd.read_pickle(f'{data_dir}/y_train.pkl')
    except FileNotFoundError:
        print("Error: Model data not found. Please run Phase 4.1 first.")
        return

    # 2. Initialize the Random Forest Classifier
    # n_estimators=100: We use 100 decision trees to ensure stability
    # random_state=42: Ensures the results are reproducible
    # n_jobs=-1: Uses all available CPU cores to speed up training
    rf_model = RandomForestClassifier(
        n_estimators=100, 
        max_depth=15, 
        random_state=42, 
        n_jobs=-1
    )

    # 3. Train the Model
    print(f"Training on {len(X_train):,} samples. This may take a moment...")
    start_time = time.time()
    
    rf_model.fit(X_train, y_train)
    
    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f"Model Training Complete! Training Time: {duration} seconds.")

    # 4. Save the Trained Model (Serialization)
    # This allows us to use the model in Phase 6 (Streamlit) without re-training
    os.makedirs('models', exist_ok=True)
    joblib.dump(rf_model, 'models/lead_scoring_model.pkl')
    
    # Save the column names to ensure the Streamlit app matches the model's input
    model_columns = list(X_train.columns)
    joblib.dump(model_columns, 'models/model_columns.pkl')

    print("\nSUCCESS: Model and metadata saved in the 'models/' directory.")

if __name__ == "__main__":
    run_model_training()