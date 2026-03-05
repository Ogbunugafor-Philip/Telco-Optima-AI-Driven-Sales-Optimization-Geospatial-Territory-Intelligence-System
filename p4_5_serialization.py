import joblib
import os
import shutil
import pandas as pd

def run_serialization_and_archiving():
    print("--- Phase 4.5: Finalizing Model Serialization & Archiving ---")

    # 1. Ensure all directories exist
    os.makedirs('models', exist_ok=True)
    os.makedirs('reports', exist_ok=True)

    # 2. Verify and Move Model Artifacts
    # We ensure the model and columns generated in 4.2 are in the right place
    if os.path.exists('models/lead_scoring_model.pkl'):
        print("Verification: 'lead_scoring_model.pkl' (The AI Brain) is ready.")
    else:
        print("Warning: Model file not found. Please ensure 4.2 ran successfully.")

    # 3. Final Summary of Production Artifacts
    print("\n--- Production Readiness Checklist ---")
    
    artifacts = {
        "AI Brain": "models/lead_scoring_model.pkl",
        "Feature Metadata": "models/model_columns.pkl",
        "Accuracy Proof": "reports/confusion_matrix.png",
        "Gap Analysis Proof": "data/viz_white_spaces.html"
    }

    all_present = True
    for name, path in artifacts.items():
        if os.path.exists(path):
            print(f" [OK] {name} confirmed at {path}")
        else:
            print(f" [MISSING] {name} NOT FOUND at {path}")
            all_present = False

    if all_present:
        print("\nSUCCESS: All serialization artifacts are secured for Phase 6 Deployment.")
        
        # 4. Create a specific Deployment Bundle (Optional but professional)
        # This copies the gaps proof into the reports folder for the final thesis
        if os.path.exists('data/viz_white_spaces.html'):
            shutil.copy('data/viz_white_spaces.html', 'reports/viz_white_space.html')
            print("Action: Copied Gap Analysis to /reports/ for project documentation.")
    else:
        print("\nAction Required: Please re-run missing steps to complete the bundle.")

if __name__ == "__main__":
    run_serialization_and_archiving()