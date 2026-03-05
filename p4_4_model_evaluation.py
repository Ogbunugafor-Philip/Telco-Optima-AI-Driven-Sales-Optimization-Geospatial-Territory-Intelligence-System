import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import os

def run_model_evaluation():
    print("--- Phase 4.4: Executing Model Evaluation & Confusion Matrix ---")

    # 1. Load the Model and the Testing Data
    try:
        model = joblib.load('models/lead_scoring_model.pkl')
        X_test = pd.read_pickle('data/model_data/X_test.pkl')
        y_test = pd.read_pickle('data/model_data/y_test.pkl')
    except FileNotFoundError:
        print("Error: Missing model or test data. Please ensure 4.1 and 4.2 ran successfully.")
        return

    # 2. Generate Predictions
    print("Running AI predictions on 105,000 unseen subscribers...")
    y_pred = model.predict(X_test)

    # 3. Calculate Scientific Metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("\n" + "="*40)
    print("     MODEL PERFORMANCE METRICS")
    print("="*40)
    print(f"Accuracy (Overall Correctness): {acc:.2%}")
    print(f"Precision (Wasted Effort Avoided): {prec:.2%}")
    print(f"Recall (Opportunities Captured): {rec:.2%}")
    print(f"F1-Score (Model Balance): {f1:.4f}")
    print("="*40)

    # 4. Plot Confusion Matrix
    print("\nGenerating Confusion Matrix visual...")
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', 
                xticklabels=['Standard User', 'High-Propensity Lead'], 
                yticklabels=['Standard User', 'High-Propensity Lead'])
    
    plt.title('Telco-Optima: Lead Scoring Confusion Matrix', fontsize=14, fontweight='bold')
    plt.ylabel('Actual Behavior (Ground Truth)', fontsize=12)
    plt.xlabel('AI Prediction (Strategic Target)', fontsize=12)
    
    # Save the report
    os.makedirs('reports', exist_ok=True)
    plt.savefig('reports/confusion_matrix.png')
    
    # 5. Business Impact Summary
    false_positives = cm[0, 1]
    true_positives = cm[1, 1]
    print(f"\nSUCCESS: Evaluation Complete.")
    print(f"- Reports saved: 'reports/confusion_matrix.png'")
    print(f"- Strategic Impact: Correctly identified {true_positives:,} high-value leads.")
    print(f"- Operational Gain: Avoided {false_positives:,} unproductive sales calls.")

if __name__ == "__main__":
    run_model_evaluation()